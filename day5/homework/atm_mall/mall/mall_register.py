#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
商城注册
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import re
import datetime
from general_module import db_operater
from general_module import db_operater
from general_module import md5_encryption
from conf import setting


# 用户注册
def user_register():
	db_file = setting.ACCOUNT_DB
	# 读取用户数据库信息
	info = db_operater.read_db(db_file)
	global name
	loop_flag = True
	while loop_flag:
		name = input("请输入用户名：").strip()
		if re.match(r'^[_a-zA-Z][_0-9a-zA-Z]{3,25}$', name):
			if not info.get(name, None):
				info[name] = {}
				while loop_flag:
					password = input("请输入密码，Q退出：").strip()
					if re.match(r'^\S{8,26}$', password):
						if password:
							password_tmp = password
							password = input("请确认您的密码：")
							if password == password_tmp:
								info[name]["password"] = md5_encryption.md5_encryption(password)
								while loop_flag:
									email = input("请输入您的邮箱地址， Q退出：").strip()
									if re.match(r'^([a-z.0-9]{1,26})@([a-z.0-9]{1,20})(.[a-z0-9]{1,8})$', email.lower()):
										info[name]["email"] = email.lower()
										info[name]["age"] = None
										info[name]["retry_count"] = 0
										info[name]["created_date"] = datetime.date.today()
										info[name]["unlock_date"] = datetime.date.today()
										# 将注册信息写入数据库
										db_operater.write_db(file=db_file, data=info)
									elif email.upper() == "Q":
										loop_flag = True
										break
									else:
										print("无效的输入，请重新输入！")
							else:
								print("两次输入的密码不一致，请重新输入！")
						else:
							print("无效的输入！请重新输入！")
					elif password.upper() == "Q":
						loop_flag = False
						break
					else:
						print("格式错误，密码必须为8-26位非空字符")
			else:
				print("用户名已存在！")
		else:
			print("格式错误，用户名格式必须为字母或下划线开头，由字母数字组成的4-26位")
	while loop_flag:
		password = input("请输入密码，Q退出：").strip()
		if re.match(r'^\S{8,26}$', password):
			if password:
				password_tmp = password
				password = input("请确认您的密码：")
				if password == password_tmp:
					info[name]["password"] = md5_encryption.md5_encryption(password)
					break
				else:
					print("两次输入的密码不一致，请重新输入！")
			else:
				print("无效的输入！请重新输入！")
		elif password.upper() == "Q":
			break
		else:
			print("格式错误，密码必须为8-26位非空字符")


# dic_demo = {}
# dic = user_register(dic_demo)
# print(dic)
# print(dic["zhangsan"]["created_date"])
# print(dic["zhangsan"]["email"])
# read_db()
