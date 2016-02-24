#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
主程序逻辑
"""

import os
import sys
import datetime
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from core import role_module
from core import save_data
from core import db_handler
from conf import setting


def get_info():
	name = input("请输入角色姓名：").strip()
	# age = input("请输入角色年龄：").strip()
	# gender = input("请输入角色性别：").strip()
	return name


# 存档
def save_game(player_object, s):
	print("正在存档...")
	print(s)
	file_name = str(datetime.datetime.now())
	db_path = db_handler.handler(setting.DATABASE, file_name)
	save_data.db_write(db_path, player_object)


# 读取存档
def read_game(file_name):
	print("正在读取...")
	db_path = db_handler.handler(setting.DATABASE, file_name)
	return save_data.db_read(db_path)


def run():
	name = get_info()
	# 初始化一个游戏角色
	a = role_module.Player(name, 22, "male", 100, 100, 2000, 50)

	print("背景：{}刚从学校毕业出来，心高气傲，准备闯出自己的一片天。。。".format(name))
	print("一天，与初中毕业的发小：<小强>一起吃饭，局间说起了各自今后的打算。")
	print("<小强>说：留在老家跟我一起烤羊肉串吧，一个月能赚不少钱呢。")
	option1 = input("1:留下来烤羊肉串 2：拒绝他")
	if option1 == "1":
		print("{}说：好啊，我正有此意！".format(a.name))
		print("从此以后{}与<小强>走上了街边卖羊肉串的道路。。。".format(a.name))
		print("5年过去了...")
		time.sleep(5)
		print("5年过去了...")
		print("或许，人这一生平平淡淡才是真...")
	elif option1 == "2":
		print("{}心想：燕雀心系檐下，鸿鹄志在苍宇。".format(a.name))
		print("{}放下酒杯对<小强>说：我要趁着年轻出去闯一闯。".format(a.name))
		print("{} 怀揣着梦想，孤身一人来到北京。")
		print("开启波澜壮阔的一生...")
		menu = "1：吃饭 2：睡觉 3：工作 4：购物 5：学习 6：存档"
		print(menu)
		option2 = input("请选择要进行的操作：")

run()
