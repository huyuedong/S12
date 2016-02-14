#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
商城注册
"""

import re
import hashlib
import pickle
import os
import datetime


# 预设一个加密算法
def md5_encryption(arg):
	try:
		# 将传入的参数按utf-8编码
		m = arg.encode("utf-8")
		# 创建添加自定义key的md5对象
		h = hashlib.md5("alex".encode("utf-8"))
		# 生成加密串
		h.update(m)
		# 返回十六进制的加密串
		return h.hexdigest()
	except TypeError:
		return None


# 读取用户数据库
def read_db(arg):
	with open(arg, "rb") as fp:
		return pickle.load(fp)


# 写入用户数据库
def write_db(file=None, data=None):
	with open(file, "wb") as fp:
		fp.write(pickle.dumps(data))


# 用户注册
def user_register(arg):
	global name
	while True:
		name = input("请输入用户名：").strip()
		if re.match(r'^[_a-zA-Z][_0-9a-zA-Z]{3,25}$', name):
			if not arg.get(name, None):
				arg[name] = {"name": name, }
				break
			else:
				print("用户名已存在！")
		else:
			print("格式错误，用户名格式必须为字母或下划线开头，由字母数字组成的4-26位")
	while True:
		password = input("请输入密码：").strip()
		if re.match(r'^\S{8,26}$', password):
			if password:
				password_tmp = password
				password = input("请确认您的密码：")
				if password == password_tmp:
					arg[name]["password"] = md5_encryption(password)
					break
				else:
					print("两次输入的密码不一致，请重新输入！")
			else:
				print("无效的输入！请重新输入！")
		else:
			print("格式错误，密码必须为8-26位非空字符")
	while True:
		email = input("请输入您的邮箱地址：").strip()
		if re.match(r'^([a-z.0-9]{1,26})@([a-z.0-9]{1,20})(.[a-z0-9]{1,8})$', email.lower()):
			arg[name]["email"] = email.lower()
			break
		else:
			print("无效的输入，请重新输入！")
	arg[name]["age"] = None
	arg[name]["retry_count"] = 0
	arg[name]["created_date"] = datetime.date.today()
	return arg

# dic_demo = {}
# dic = user_register(dic_demo)
# print(dic)
# print(dic["zhangsan"]["created_date"])
# print(dic["zhangsan"]["email"])
# read_db()
