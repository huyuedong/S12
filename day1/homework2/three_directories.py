#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
多级菜单
-三级菜单
-可依次选择进入各子菜单
-所需新知识点：列表、字典
"""

import get_user_input


city_dict = {
	"北京": {
		"朝阳区": ["国贸", "望京", "三里屯"],
		"海淀区": ["五道口", "中关村", "学院路"],
		"昌平区": ["沙河", "天通苑", "回龙观"]
	},
	"上海": {
		"静安区": ["静安寺", "梅恒泰", "大中里太古城"],
		"黄浦区": ["人民广场", "外滩", "豫园"],
		"徐汇区": ["中山公园", "天山路商圈", "古北路商圈"]
	},
	"香港": {
		"旺仔": ["铜锣湾", "跑马地", "大坑"],
		"油尖旺": ["尖沙咀", "旺角", "佐敦"],
		"西贡": ["清水湾", "将军澳", "北潭涌"]
	}
}

loop_flag = True    # 定义循环标志
while loop_flag:    # 定义第一级菜单的循环
	print("第一级目录：")
	level1_list = []
	for i in iter(city_dict):
		level1_list.append(i)   # 生成第一级菜单的列表
	for i, val in enumerate(level1_list, 1):
		print("%s.%s" % (i, val))  # 打印出一级菜单

	a = get_user_input.get_user_input(1, level1_list)   # 获取用户输入
	if a == 'Q':
		print("您的选择是退出本系统！")
		loop_flag = False
		break
	else:
		print("您的选择是%s，其子目录是：" % a)
		while loop_flag:    # 定义第二级目录循环
			level2_list = []    # 初始化二级目录列表
			for i in iter(city_dict[a]):
				level2_list.append(i)   # 生成二级目录列表
			for i, val in enumerate(level2_list, 1):
				print("%s.%s" % (i, val))  # 打印对应的二级目录

			b = get_user_input.get_user_input(2, level2_list)   # 获取用户输入
			if b == 'B':
				print("您的选择是回到上一级菜单！")
				break   # 跳出while循环
			elif b == 'Q':
				print("您的选择是退出本系统！")
				loop_flag = False   # 准备跳出外层while循环
				break   # 跳出本层while循环
			else:
				print("您的选择是%s，其子目录是：" % b)
				while loop_flag:
					level3_list = city_dict[a][b]   # 生成三级菜单列表
					for i, val in enumerate(level3_list, 1):
						print("%s.%s" % (i, val))  # 打印对应的三级菜单
					c = get_user_input.get_user_input(3, level3_list)   # 获取用户输入
					if c == 'B':
						print("您的选择是回到上一级菜单！")
						break   # 跳出本层while循环
					else:
						print("您的选择是退出本系统！")
						loop_flag = False   # 准备跳出最外层while循环
						break   # 跳出本层while循环
