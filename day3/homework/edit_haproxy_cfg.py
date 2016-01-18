#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
通过python程序可以对ha配置文件进行增删改，不再是以往的打开文件进行直接操作。
"""
import json
line_list = []
line2_list = []


# 初始化配置文件
def init_cfg():
	with open('haproxy.cfg', 'r') as f:
		for line in f.readlines():
			line_info = line.rstrip()
			if line_info.startswith(' '):
				line2_list.append(line_info.strip())
			else:
				line_list.append(line_info.strip())
	return line_list, line2_list
n = init_cfg()
print(n)


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


# 打印分项菜单
def print_info(tag):
	while True:
		if tag == 1:
			read = input("请输入backend:").strip()
			read = json.loads(read)
			return read
		elif tag == 2:
			read = input("请输入要新加的记录：").strip()
			read = json.loads(read)
			return read
		elif tag == 3:
			read = input("请输入要删除的记录：").strip()
			read = json.loads(read)
			return read
