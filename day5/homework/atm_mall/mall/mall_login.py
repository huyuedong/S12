#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
购物商城的登录
"""

import os
import sys
import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from general_module import db_operater
from general_module import db_operater
from general_module import md5_encryption


def mall_login(func):
	def wrapper():
		print("想购物，先登录。。。")
		db_file_tmp = "{}/database/account.db".format(os.path.dirname(os.path.dirname(__file__)))
		db_file = os.path.abspath(db_file_tmp)
		info = db_operater.read_db(db_file)
		for i in info:
			if info[i]["unlock_date"] <= datetime.date.today():
				info[i]["unlock_date"] = datetime.date.today()
				info[i]["retry_count"] = 0
		while True:
			user_name = input("请输入用户名：").strip()
			password = input("请输入密码：").strip()
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
			else:
				print("用户名不存在，请重新输入！")
		db_operater.write_db(file=db_file, data=info)
	return wrapper
