#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
实现删除配置文件下指定url下的server信息（server下为空时删除该记录）
	-输入：
		arg = {
			'backend': 'www.oldboy.org',
			'record':{
				'server': '100.1.7.9',
				'weight': 20,
				'maxconn': 30
			}
		}
	-删除对应backend下的信息

"""
import json


# 获取用户输入的删除条目
def get_delete_index():
	while True:
		delete_num = input("{}的配置信息如下，请选择你要删除的记录序号：".format(arg))
		for num, i in enumerate(server_list, 1):
			print("{}.{}".format(num, i))
		if delete_num.isdigit():
			delete_index = int(delete_num)
			if 0 < delete_index <= len(server_list):
				return delete_num - 1
			else:
				print("Invalid input,Please try again!")
		else:
			print("Invalid input,Please try again!")


# 删除菜单
def del_menu():
	while True:
		input_title = input("Please input the title of the backend you want to delete:").strip()
		# 判断用户输入的title是否为有效格式
		if all([len(input_title.split('.')) == 3, input_title.split('.')[2] in string.ascii_letters]):
			break
		else:
			print("Invalid input,please try again!")

	server_list = show_info(input_title)
	delete_index = get_delete_index()
	server_list.pop(delete_index)
	if server_list:
		# server_list不为空的时候，写入配置
		# 更新配置文件
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
	# server_list为空时，则删除对应的backend项
	else:
		with open('haproxy.cfg', 'r+') as f1, open('haproxy.new', 'w+') as f2:
			flag = True
			for line in f1:
				if line.strip() == "backend {}".format(input_title):
					flag = False
					continue
				elif line.strip().startswith("backend"):
					flag = True
				elif all([flag, line]):
					f2.write(line)

