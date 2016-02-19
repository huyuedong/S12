#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
购物商城的登录
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import datetime
import mall_register
from general_module import db_operater
from general_module import db_operater
from general_module import md5_encryption
from conf import setting


def mall_login(func):
	def wrapper():
		print("想购物，先登录。。。")
		db_file = setting.MALL_ACCOUNT_DB
		info = db_operater.read_db(db_file)
		for i in info:
			if info[i]["unlock_date"] <= datetime.date.today():
				info[i]["unlock_date"] = datetime.date.today()
				info[i]["retry_count"] = 0
		loop_flag = True
		while loop_flag:
			option = input("1.登录 2.注册 Q.退出：")
			if option == "1":
				while loop_flag:
					user_name = input("请输入用户名，B返回Q退出：").strip()
					password = input("请输入密码， B返回Q退出：").strip()
					if info.get(user_name, None):
						if info[user_name]["retry_count"] < 3:
							if md5_encryption.md5_encryption(password) == info[user_name].get("password", None):
								print("welcome you {}!".format(user_name))
								func()
								break
							else:
								info[user_name]["retry_count"] += 1
								print("密码错误，请重新输入！")
						else:
							print("该用户名已被锁定，请明天再试！")
							if info[user_name]["unlock_date"] <= datetime.date.today():
								info[user_name]["unlock_date"] += datetime.timedelta(days=1)
								break
							else:
								break
					elif user_name.upper() == "B":
						break
					elif user_name.upper() == "Q":
						loop_flag = False
						break
					else:
						print("用户名不存在，请重新输入！")
			elif option == "2":
				print("这是qimi商城注册界面：")
				mall_register.user_register()
			elif option.upper() == "Q":
				break
		db_operater.write_db(file=db_file, data=info)
	return wrapper
