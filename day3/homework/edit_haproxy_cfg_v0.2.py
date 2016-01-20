#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作。
"""
import json
import os
from collections import OrderedDict


# 获取用户输入
def get_user_input():
	while True:
		print("""
		Welcome to the menu of operate HAProxy.cfg：
		1.Check out the records of backend!
		2.Edit the records of backend!
		3.Remove some records of the backend!
		4.Quit!
		""")
		user_choose = input("Please input the serial number of your choice：").strip()
		if user_choose.isdigit():
			user_choose = int(user_choose)
			if user_choose == 1:
				print("Your choice is ：1.Check out the records of backend!")
				return 1
			elif user_choose == 2:
				print("Your choice is ：2.Edit the records of backend!")
				return 2
			elif user_choose == 3:
				print("Your choice is ：3.Remove some records of the backend!")
				return 3
			elif user_choose == 4:
				print("Your choice is ：4.Quit!")
				return 4
			else:
				print("Invalid input, please try again!")
		else:
			print("Invalid input, please try again!")


# 获取用户输入的供查询的url
def get_url_info():
	while True:
		url = input("Please input the url you want to check:").strip()
		n = url.count('.')
		if n:
			if all([n == 2, url.split('.')[2].isalpha()]):
				return url
		else:
			print("invalid url，please try again!")


# 查看配置信息
def show_info(url):
	server_list = []
	with open('haproxy.cfg') as f:
		flag = False
		for line in f:
			# 匹配到用户输入的url时,开始统计server信息
			if line.rstrip() == 'backend {}'.format(url):
				flag = True
				continue
			# 匹配到下一条backend时就退出
			elif line.startswith('backend'):
				flag = False
				continue
			# 将符合条件的server信息录入列表
			elif all([line.startswith(' '), line, flag]):
				server_list.append(line.strip())
	return server_list


def init_backend_info():
	dic_tmp = OrderedDict()
	with open('haproxy.cfg', 'r') as f:
		n = 1
		flag = False
		n_flag = False
		for line in f:
			if line.strip().startswith('backend'):
				dic_tmp[n] = []
				dic_tmp[n].append(line.strip()[1])
				flag = True
				n_flag = True
				continue
			elif all([flag, line.strip().startswith("server")]):
				dic_tmp[n].append(line.strip())
				n_flag = False
			elif all([flag, n_flag]):
				n += 1
			else:
				continue
	return dic_tmp


# 增加配置信息
def add_menu():
	# 打印一个输入示例供输入时复制修改。
	print('eq：{"backend": "www.oldboy.org", "record": {"server": "100.1.7.99", "maxconn": 30, "weight": 20}}')
	arg = input("Please input the cfg you want to change:")
	arg = json.loads(arg)
	server_list = show_info(arg.get('backend'))
	d1 = arg.get('record')
	# 如果用户输入server时输入hostname和IP的话可以使用reduce
	# d1 = arg.get('record')
	# l1 = []
	# for k, v in d1.items():
	# 	l1.append("{} {}".format(k, v))
	# list_demo = reduce(lambda x, y: "{} {}".format(x, y), l1)
	list_demo = "server {} {} weight {} maxconn {}".format(d1.get('server'), d1.get('server'), d1.get('weight'), d1.get('maxconn'))
	# 原来无此项配置记录时需要新建backend记录
	if len(server_list) == 0:
		with open('haproxy.cfg', 'a+') as f:
			f.write("backend {}\n".format(arg.get('backend')))
			f.write("{}{}\n".format(' ' * 8, list_demo))
			f.flush()
		# 打印修改后的配置信息

	# 原来有该配置项记录时，将新输入的内容加入配置列表再写入文件
	else:
		# 原来的server信息已存在时打印重复提示
		print(list_demo)
		print(server_list)
		if list_demo in server_list:
			print("The record you input is already exist!")
		# 新加的server信息不存在则写入
		else:
			server_list.append(list_demo)
			with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
				stop_flag = True
				start_flag = False
				for line in f1:
					if line.strip() == "backend {}".format(arg.get('backend')):
						f2.write(line)
						start_flag = True
						stop_flag = False
						continue
					elif line.startswith("backend"):
						f2.write(line)
						stop_flag = True
						continue
					elif all([start_flag, not stop_flag]):
						start_flag = False
						for i in server_list:
							f2.write("{}{}\n".format(' ' * 8, i))
					elif all([not start_flag, stop_flag, line]):
						f2.write(line)
				f1.flush()
				f2.flush()
			# 将原配置文件备份
			os.rename('haproxy.cfg', 'haproxy.bak')
			# 将新配置文件
			os.rename('haproxy.new', 'haproxy.cfg')
			# 删除旧的备份文件
			os.remove('haproxy.bak')


# 获取用户输入的删除条目
def get_delete_index(server_list):
	while True:
		for num, i in enumerate(server_list, 1):
			print("{}.{}".format(num, i))
		delete_num = input("Please input the number of record you want to delete：")
		if delete_num.isdigit():
			delete_num = int(delete_num)
			if 0 < delete_num <= len(server_list):
				return delete_num - 1
			else:
				print("Invalid input,Please try again!")
		else:
			print("Invalid input,Please try again!")


# 删除菜单
def del_menu(input_title):
	server_list = show_info(input_title)
	delete_index = get_delete_index(server_list)
	delete_title = server_list[delete_index]
	server_list.pop(delete_index)
	if server_list:
		# server_list不为空的时候，写入配置
		with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
			flag = True
			for line in f1:
				if line.strip() == "backend {}".format(input_title):
					f2.write(line)
					flag = False
					for i in server_list:
						f2.write("{}{}\n".format(' ' * 8, i))
				elif line.startswith("backend"):
					f2.write(line)
					flag = True
				elif all([flag, line]):
					f2.write(line)
			f1.flush()
			f2.flush()
		# 将原配置文件备份
		os.rename('haproxy.cfg', 'haproxy.bak')
		# 将新配置文件
		os.rename('haproxy.new', 'haproxy.cfg')
		# 删除旧的配置文件
		os.remove('haproxy.bak')
	# server_list为空时，则删除对应的backend项
	else:
		with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
			# flag = True
			for line in f1:
				# 删除backend项
				if line.strip() == "backend {}".format(input_title):
					# flag = False
					continue
				# 删除server 信息
				elif line.strip() == delete_title:
					continue
				else:
					f2.write(line)
			f1.flush()
			f2.flush()
		# 将原配置文件备份
		os.rename('haproxy.cfg', 'haproxy.bak')
		# 将新配置文件
		os.rename('haproxy.new', 'haproxy.cfg')
		# 将原配置文件删除
		os.remove('haproxy.bak')


# 主函数
def main():
	while True:
		num = get_user_input()
		# 查看
		if num == 1:
			ur = get_url_info()
			server_list = show_info(ur)
			if len(server_list) == 0:
				print("Sorry,there is no records about your input!")
			else:
				for i in server_list:
					print(i)
		# 修改或增加
		elif num == 2:
			add_menu()
		# 删除
		elif num == 3:
			url = get_url_info()
			del_menu(url)
		# 退出
		elif num == 4:
			print("Good Bye~")
			break

if __name__ == '__main__':
	main()
