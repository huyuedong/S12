#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
主程序逻辑
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from core import role_module


def get_info():
	name = input("请输入角色姓名：").strip()
	# age = input("请输入角色年龄：").strip()
	# gender = input("请输入角色性别：").strip()
	return name


def run():
	name = get_info()
	# 初始化一个游戏角色
	a = role_module.Player(name, 22, "male", 100, 100, 2000, 50)

	print("背景：{}刚从学校毕业出来，心高气傲，准备创出自己的一片天。。。".format(name))
	print("朋友说：留在老家跟我一起烤羊肉串吧，一个月能赚不少钱呢。")
	option1 = input("1:留下来烤羊肉串 2：拒绝他")
	if option1 == "1":
		print("{}说：好啊，我正有此意！".format(name))
	elif option1 == "2":
		print("{}说：燕雀心系檐下，鸿鹄志在苍宇。我要趁着年轻出去闯一闯。".format(name))

run()