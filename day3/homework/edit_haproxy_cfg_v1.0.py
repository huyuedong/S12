#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作。
version 1.0
-增加二级菜单回退功能
-在查看配置信息菜单增加回车直接打印当前所有backend配置信息
-修改、删除操作完成后，改为默认回到主菜单。
-代码结构优化，增加注释。
-修复几处bug
-*修复用户添加配置信息时，输入非json可以解析的有效数据时程序非正常退出的bug
-*修复了用户删除配置信息时，输入不存在的url时，没有提示信息的bug
-*修复了get_url_info()中输入不正确的网址格式时没有跳出并提示用户的bug
"""
import json
import os
from collections import OrderedDict


# 获取用户输入
def get_user_input():
	while True:
		print("这是操作haproxy.cfg文件的小程序：".center(50, '*'))
		print("""
				1.查看后台配置信息。
				2.添加后台配置信息。
				3.删除后台配置信息。
				4.退出。
		""")
		print("-" * 60)
		user_choose = input("请输入你要进行的操作对应的序号：").strip()
		if user_choose.isdigit():
			user_choose = int(user_choose)
			if user_choose == 1:
				print("您的选择是：1.查看后台配置信息!")
				return 1
			elif user_choose == 2:
				print("您的选择是：2.添加后台配置信息!")
				return 2
			elif user_choose == 3:
				print("您的选择是：3.删除后台配置信息!")
				return 3
			elif user_choose == 4:
				print("您的选择是：4.退出!")
				return 4
			else:
				print("错误的输入，请重新输入！")
		else:
			print("错误的输入，请重新输入！")


# 获取用户输入的供查询的url
def get_url_info():
	while True:
		url = input("请输入要操作的url（B返回上级菜单，查询菜单下可直接回车查看当前所有backend信息）:").strip()
		n = url.count('.')
		# 判断输入是否为有效的url
		if n:
			# 判断输入的是否为有效url格式
			try:
				if all([n == 2, url.split('.')[2].isalpha()]):
					return url
			except IndexError:
				print("错误的输入，请重新输入！")
		elif url.upper() == "B":
			return "B"
		# 输入回车或空格返回“ENTER”,准备打印所有backend信息
		elif url == "":
			return "ENTER"
		else:
			print("错误的url，请重新输入！")


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


# 查看当前backend配置信息
def init_backend_info():
	dic_tmp = {}
	with open('haproxy.cfg', 'r') as f:
		n = 0
		flag = False
		for line in f:
			if line.strip().startswith('backend'):
				n += 1
				dic_tmp[n] = []
				dic_tmp[n].append(line.split()[1])
				flag = True
			elif all([flag, line.strip().startswith("server")]):
				dic_tmp[n].append(line.strip())
				continue
	backend_dic = OrderedDict()
	for i in dic_tmp.items():
		tmp = i[1][0]
		i[1].pop(0)
		backend_dic[tmp] = i[1]
	print("当前backend配置信息如下：")
	for k in backend_dic.keys():
		print("backend {}".format(k))
		for v in backend_dic.get(k):
			print("{}{}".format(" " * 8, v))
		print("\n")


# 增加配置信息
def add_menu(arg):
	server_list = show_info(arg.get('backend'))
	d1 = arg.get('record')
	# 如果用户输入server时输入hostname和IP的话可以使用reduce
	# d1 = arg.get('record')
	# l1 = []
	# for k, v in d1.items():
	# 	l1.append("{} {}".format(k, v))
	# list_demo = reduce(lambda x, y: "{} {}".format(x, y), l1)
	l_tmp = [d1.get('server'), d1.get('server'), d1.get('weight'), d1.get('maxconn')]
	list_demo = "server {} {} weight {} maxconn {}".format(* l_tmp)
	# 原来无此项配置记录时需要新建backend记录
	if len(server_list) == 0:
		with open('haproxy.cfg', 'a+') as f:
			f.write("backend {}\n".format(arg.get('backend')))
			f.write("{}{}\n".format(' ' * 8, list_demo))
			f.flush()
		print("添加成功！")
		# 打印修改后的配置信息
		init_backend_info()

	# 原来有该配置项记录时，将新输入的内容加入配置列表再写入文件
	else:
		# 添加的server信息已存在时打印重复提示
		if list_demo in server_list:
			print("该配置信息已存在！")
		# 新加的server信息不存在则写入
		else:
			server_list.append(list_demo)
			with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
				# 定义一个停止从server_list取数据写入的标签
				stop_flag = True
				# 定义一个开始从server_list取数据写入的标签
				start_flag = False
				for line in f1:
					# 此处的if(elif)判断从上到下，如果一个判断满足则后面的判断均不再执行
					# 匹配到backend记录时，将开始标签置为真，结束标签置为否
					if line.strip() == "backend {}".format(arg.get('backend')):
						f2.write(line)
						start_flag = True
						stop_flag = False
						continue
					# 匹配到下一条backend记录时，将结束标签置为真
					elif line.startswith("backend"):
						f2.write(line)
						stop_flag = True
						continue
					# 当开始标签为真，结束标签为假时，从server_list取值写入，并把开始标签置为假
					elif all([start_flag, not stop_flag]):
						start_flag = False
						for i in server_list:
							f2.write("{}{}\n".format(' ' * 8, i))
					# 当开始标签为假且结束标签为真时，从原配置文件取值写入
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
			print("添加成功！")
			init_backend_info()


# 获取用户输入的删除条目
def get_delete_index(server_list):
	while True:
		for num, i in enumerate(server_list, 1):
			print("{}.{}".format(num, i))
		delete_num = input("请输入要删除的记录对应的序号：")
		if delete_num.isdigit():
			delete_num = int(delete_num)
			if 0 < delete_num <= len(server_list):
				return delete_num - 1
			else:
				print("错误的输入，请重新输入！")
		else:
			print("错误的输入，请重新输入！")


# 删除菜单
def del_menu(server_list, input_title):

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
		print("配置信息删除成功！")
		init_backend_info()
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
		print("配置文件删除成功！因为server配置项为空，backend {}记录已删除。".format(input_title))
		init_backend_info()


# 主函数
def main():
	while True:
		num = get_user_input()
		# 查看
		if num == 1:
			while True:
				ur = get_url_info()
				if ur == "B":
					break
				# 打印所有backend信息
				if ur == "ENTER":
					init_backend_info()
					break
				else:
					server_list = show_info(ur)
					if len(server_list) == 0:
						print("找不到要查询的记录！")
					else:
						for i in server_list:
							print(i)
						break
		# 修改或增加
		elif num == 2:
			while True:
				# 打印一个输入示例供输入时复制修改。
				print('例如=>：{"backend": "www.oldboy.org", "record": {"server": "100.1.7.99", "maxconn": 30, "weight": 20}}')
				arg = input("请输入要添加的配置信息（'B'返回上一级）:").strip()
				if arg.upper() == 'B':
					break
				else:
					# 如果json解析不了就让用户重新输入
					try:
						arg = json.loads(arg)
						add_menu(arg)
						break
					except json.decoder.JSONDecodeError:
						print("无效的输入，请重新输入！")
		# 删除
		elif num == 3:
			while True:
				ur = get_url_info()
				# 返回上一级菜单。
				if ur == "B":
					break
				else:
					server_list = show_info(ur)
					# 输入的网址存在，打印该网址下的server信息。
					if server_list:
						del_menu(server_list, ur)
						break
					# 输入的网址不存在时，打印提示信息。
					else:
						print("您输入的后台网址不存在，请重新输入！")
		# 退出
		elif num == 4:
			print("再见~")
			break

if __name__ == '__main__':
	main()
