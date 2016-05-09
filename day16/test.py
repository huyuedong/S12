#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

for i in range(3):
	flag = False
	user = input("请输入账号：")
	passwd = input("请输入密码：")
	with open("user_passwd", "r") as f:
		for line in f:
			line = line.strip("\n")
			if line.split()[0] == user and line.split()[1] == passwd:
				print("欢迎登陆")
				flag = True
				break
		else:
			print("您输入的账号不存在或密码错误")
	if flag:
		break
else:
	print("您尝试过多，已被锁定")
