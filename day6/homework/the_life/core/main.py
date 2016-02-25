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
from core import compute_value


def get_info():
	name = input("请输入角色姓名：").strip()
	# age = input("请输入角色年龄：").strip()
	# gender = input("请输入角色性别：").strip()
	return name


# 存档
def save_game(player_object):
	print("正在存档...")
	# 生成一个以当前时间为文件名的存档文件
	file_name = time.strftime('%Y%m%d_%H%M%S', time.gmtime(time.time()))
	db_path = db_handler.handler(setting.DATABASE, file_name)

	save_data.db_write(db_path, player_object)


# 读取存档
def read_game(file_name):
	print("正在读取...")
	db_path = db_handler.handler(setting.DATABASE, file_name)
	return save_data.db_read(db_path)


def get_option(player_object):
	menu = "1：吃饭 2：睡觉 3：工作 4：购物 5：学习 6：存档"
	menu_dic = {
		"1": {"option": "接下来要：吃饭", "action": player_object.to_eat},
		"2": {"option": "接下来要：睡觉", "action": player_object.to_sleep},
		"3": {"option": "接下来要：工作", "action": player_object.work},
		"4": {"option": "接下来要：购物", "action": player_object.consume},
		"5": {"option": "接下来要：学习", "action": player_object.learn},
		"6": {"option": "接下来要：存档", "action": save_game},
			}
	exit_flag = False
	while not exit_flag:
		print(menu)
		option = input("==>").strip()
		if option in menu_dic:
			if option == "1":
				player_object.to_eat("包子")
				player_object = compute_value.compute_value(player_object, "eat", 1)
			elif option == "2":
				player_object.to_sleep()
		else:
			print("选项不存在！")


def run():
	# 获取用户输入的角色名
	name = get_info()
	# 初始化一个游戏角色
	player = role_module.Player(name, 22, "male", 100, 100, 2000, 50)

	print("背景：{}刚从学校毕业出来，心高气傲，准备闯出自己的一片天。。。".format(name))
	print("一天，与初中毕业的发小：<阿强> 一起吃饭，局间说起了各自今后的打算。")
	aqiang = role_module.Role("阿强", 22, "male")
	aqiang.say("留在老家跟我一起烤羊肉串吧，一个月能赚不少钱呢。")
	option1 = input("1:留下来烤羊肉串 2：拒绝他")
	if option1 == "1":
		player.say("好啊，我正有此意！")
		print("从此以后 {} 与 {} 走上了街边卖羊肉串的道路。。。".format(player.name, aqiang.name))
		print("5年过去了...")
		time.sleep(5)
		print("又5年过去了...")
		print("或许，人这一生平平淡淡才是真...")
		print("Game Over!")
	elif option1 == "2":
		player.think("燕雀心系檐下，鸿鹄志在苍宇。")
		player.say("我要趁着年轻出去闯一闯。", "放下酒杯")
		print("{} 怀揣着梦想，孤身一人来到北京。".format(player.name))
		print("开启波澜壮阔的一生...")
		player_action = get_option(player)
		player_action("Python", 1)

run()
