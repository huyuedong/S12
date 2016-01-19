#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作。
"""
import string
import json


# 获取用户输入
def get_user_input():
	while True:
		print("""
		欢迎进入HAProxy.cfg菜单：
		1.查看当前HAProxy配置记录
		2.增加HAProxy记录信息
		3.删除HAProxy记录信息
		4.退出
		""")
		user_choose = input("请输入操作序号：").strip()
		if user_choose.isdigit():
			user_choose = int(user_choose)
			if user_choose == 1:
				print("您的选择是：1.查看当前HAProxy配置记录")
				return 1
			elif user_choose == 2:
				print("您的选择是：2.增加HAProxy记录信息")
				return 2
			elif user_choose == 3:
				print("您的选择是：3.删除HAProxy记录信息")
				return 3
			elif user_choose == 4:
				print("您的选择是：4.退出")
				return 4
			else:
				print("无效的输入，请重新输入！")
		else:
			print("无效的输入，请重新输入！")


# 获取用户输入的供查询的url
def get_url_info():
	while True:
		url = input("Please input the url you want to check:").strip()
		if len(url.split('.')) == 3:
			if url.split('.')[2] in string.ascii_letters:
				return url
		else:
			print("invalid url，please try again!")


# 查看配置信息
def show_info(url):
	server_list = []
	with open('haproxy.cfg') as f:
		flag = False
		for i in f.readlines():
			# 匹配到用户输入的url时,开始统计server信息
			if i.rstrip() == 'backend {}'.format(url):
				flag = True
				continue
			# 匹配到下一条backend时就退出
			elif i.startswith('backend'):
				break
			# 将符合条件的server信息录入列表
			elif all([i.startswith(' '), i, flag]):
				server_list.append(i.strip())
		return server_list


# 增加配置信息
def add_menu():
	arg = input("Please input the cfg you want to change:")
	arg = json.loads(arg)
	server_list = show_info(arg.get('backend'))
	# 原来无此项配置记录时需要新建backend记录
	if len(server_list) == 0:
		pass
		# flag = True
		# with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
		# 	for line in f1:
		# 		if line.strip() == "backend {}".format(arg.get("backend")):
		# 			f2.write(line)
		# 			flag = False
		# 			for i in server_list:
		# 				f2.write("{}{}\n".format(' ' * 8, i))
		# 		elif line.startswith("backend"):
		# 			f2.write(line)
		# 			flag = True
		# 		elif all([flag, line]):
		# 			f2.write(line)
	else:
		server_list.append(arg.get('record'))
		flag = True
		with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
			for line in f1:
				if line.strip() == "backend {}".format(arg.get("backend")):
					f2.write(line)
					flag = False
					for i in server_list:
						f2.write("{}{}\n".format(' ' * 8, i))
				elif line.startswith("backend"):
					f2.write(line)
					flag = True
				elif all([flag, line]):
					f2.write(line)


# 主函数
def main():
	num = get_user_input()
	if num == 1:
		ur = get_url_info()
		server_list = show_info(ur)
		if len(server_list) == 0:
			print("Sorry,there is no records about your input!")
		else:
			for i in server_list:
				print(i)


if __name__ == '__main__':
	main()
