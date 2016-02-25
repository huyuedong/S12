#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
主程序逻辑
"""

import os
import sys
import re
import time
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from core import role_module
from core import save_data
from core import db_handler
from conf import setting


# 显示存档文件
def show_save():
	base_path = "{}\db".format(os.path.dirname(os.path.dirname(__file__)))
	l1 = os.listdir(base_path)
	# 定义一个保存存档的列表
	save_list = []
	for i in l1:
		# 将目录下有效的存档添加到列表中
		if re.match(r'^\d{8}_\d{6}$', i):
			save_list.append(i)
	# 打印存档选项
	for k, v in enumerate(save_list, 1):
		print("{}:{}".format(k, v))
	while True:
		option = input("请输入你要load的存档：").strip()
		if option.isdigit():
			option = int(option)
			if option <= len(save_list):
				return save_list[option-1]
			else:
				print("无效的输入，请重新输入！")
		else:
			print("无效的输入，请重新输入！")


# 游戏入口
def get_info():
	while True:
		print("1.创建角色 2.读取存档 3.退出")
		option = input("==>").strip()
		if option == "1":
			name = input("请输入角色姓名：").strip()
			player = role_module.Player(name, 22, "male", 100, 100, 2000, 10, 50)
			print("暂时默认：性别男，体力值100，精力值100，现金2000元，信心值50。")
			print("背景：{}刚从学校毕业出来，心高气傲，准备闯出自己的一片天。。。".format(player.name))
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
			return player
		elif option == "2":
			choose_save = show_save()
			return read_game(choose_save)
		elif option == "3":
			exit("Bye~")
		else:
			print("无效的输入，请重新输入！")


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


# 游戏内容
def get_option(player_object):
	menu = "1：吃饭 2：睡觉 3：工作 4：购物 5：学习 6：存档 7：退出游戏"
	menu_dic = {
		"1": {"option": "吃饭", "action": player_object.to_eat},
		"2": {"option": "睡觉", "action": player_object.to_sleep},
		"3": {"option": "工作", "action": player_object.work},
		"4": {"option": "购物", "action": player_object.consume},
		"5": {"option": "学习", "action": player_object.learn},
		"6": {"option": "存档", "action": player_object.save_game},
		"7": {"option": "退出", "action": exit}
			}
	exit_flag = False
	while not exit_flag:
		print(menu)
		option = input("==>").strip()
		if option in menu_dic:
			temp_obj = menu_dic[option].get("action")
			temp_obj()
			if player_object.get_attr("confidence") > 20000:
				print("{} 利用业余时间，开发了一款名为：the life 的游戏，风靡全球...".format(player_object.name))
				print("当他回老家度假的时候，约阿强一起吃饭，这时候的阿强已经在老家烤了10年的羊肉串...")
				print("席间，阿强拿出他的手机对{}说：你玩过那个叫the life的游戏吗，我在里面已经混到霸道总裁了。".format(player_object.name))
				print("{} 看着阿强的手机屏幕，并没有说话...".format(player_object.name))
				print("...")
				time.sleep(5)
				print("...")
				print("Game Over")
		else:
			print("选项不存在！")


# 运行游戏
def run():
	# 获取用户输入的角色名
	player = get_info()
	player.show_info()
	print("请继续游戏...")
	get_option(player)

