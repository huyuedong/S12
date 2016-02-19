#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting
from general_module import db_operater
from general_module import md5_encryption


# 简易登录验证
def login(arg):
	def outter(func):
		def wrapper():
			loop_flag = True
			while loop_flag:
				# 访问用户数据库
				if arg == 1:
					db = db_operater.read_db(setting.ACCOUNT_DB)
				# 访问管理员数据库
				elif arg == 2:
					db = db_operater.read_db(setting.ADMIN_DB)
				else:
					print("调用时出现参数错误！")
				card_id = input("请输入卡号，Q退出：").strip()
				password = input("请输入密码，Q退出：").strip()
				if card_id.upper() == "Q":
					break
				elif db.get(card_id):
					if md5_encryption.md5_encryption(password) == db[card_id].get("password", None):
						func(card_id)
				else:
					print("无效的输入或密码错误！")
		return wrapper
	return outter
