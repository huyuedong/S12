#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


def get_user_input(level_num, level_list):
	"""
	:param level_num: 用于确定调用函数时所处的菜单级别，第一级菜单无‘B’选项；第三级菜单无下一级选项
	:param level_list: 用于确定每一级的菜单列表
	:return: 返回用户的选择

	"""
	while True:
		if level_num == 1:  # 调用处于第一季菜单时
			user_input = input("请输入相应数字，Q退出本系统：").strip()   # 获取用户输入，去掉两头的空格
			if user_input.isdigit():    # 判断用户输入是否为数字
				user_input = int(user_input)    # 是数字就转换成int类型
				if user_input <= len(level_list):   # 判断用户的输入是否为有效的数字
					return level_list[user_input - 1]   # 是有效的数字就返回用户输入的数字转换为具体名称返回
				else:
					print("无效的输入！请重新输入！")   # 打印提示信息，继续请求输入
			elif user_input.upper() == 'Q':
				return 'Q'
			else:
				print("无效的输入！请重新输入！")
		elif level_num == 2:    # 当调用处于第二级菜单时
			user_input = input("请输入相应数字，B回到上一级菜单，Q退出本系统：").strip()
			if user_input.isdigit():
				user_input = int(user_input)
				if user_input <= len(level_list):
					return level_list[user_input - 1]
				else:
					print("无效的输入！请重新输入！")
			elif user_input.upper() == 'B':
				return 'B'  # 第二级菜单比第一级菜单多了一个B选项
			elif user_input.upper() == 'Q':
				return 'Q'
			else:
				print("无效的输入，请重新输入！")
		elif level_num == 3:    # 当调用处于第三季菜单时
			user_input = input("B回到上一级菜单，Q退出本系统：").strip()
			if user_input.upper() == 'B':
				return 'B'
			elif user_input.upper() == 'Q':
				return 'Q'
			else:
				print("无效的输入！请重新输入：")   # 第三级菜单无下一级菜单
		else:
			print("调用时出现参数错误！")
