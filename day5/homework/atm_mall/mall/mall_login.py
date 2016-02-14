#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
购物商城的登录
"""
import os
from mall_register import read_db
from mall_register import write_db
from mall_register import md5_encryption


def mall_login():
	db_file_tmp = "{}/database/account.db".format(os.path.dirname(os.path.dirname(__file__)))
	db_file = os.path.abspath(db_file_tmp)
	info = read_db(db_file)
	while True:
		user_name = input("请输入用户名：").strip()
		password = input("请输入密码：").strip()
		if info.get(user_name, None):
			if info[user_name]["retry_count"] < 3:
				if md5_encryption(password) == info[user_name].get("password", None):
					print("welcome!")
					break
				else:
					info[user_name]["retry_count"] += 1
					print("密码错误，请重新输入！")
			else:
				print("该用户名已被锁定，请明天再试！")
				break
		else:
			print("用户名不存在，请重新输入！")
	write_db(file=db_file, data=info)

mall_login()
