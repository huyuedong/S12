#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
管理员的具体操作实现代码
"""


def login():
	"""
	堡垒机登陆功能
	:return:
	"""
	count = 0
	while count < 3:
		username = input("UserName:").strip()
		if len(username) == 0:
			continue
		password = input("PassWord:").strip()

