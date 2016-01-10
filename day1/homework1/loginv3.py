#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
	编写登陆接口
		-输入用户名和密码
		-认证成功后显示欢迎信息
		-输错三次密码锁定相应用户
		*在v2版的基础上修复第三次输入的用户名与前两次不同时，第三次的用户名被锁定的bug!
		**增加一个变量用于存储用户名输入密码错误的次数
"""

account_file = "account.txt"
lock_file = "lock.txt"
account_list = []
lock_list = []


