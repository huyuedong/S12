#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django.shortcuts import redirect
import hashlib
from cmdb import models


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


# 认证
def verify(email, password):
	pwd = md5_encryption(password)
	user_obj = models.UserInfo.objects.filter(email=email, password=pwd)
	if user_obj:
		return user_obj
	else:
		return None


# 判断是否登陆过
def acc_auth(func):
	def check_login(request, **kwargs):
		login_stat = request.session.get("IS_LOGIN", 0)
		if login_stat == 1:
			return func(request, **kwargs)
		else:
			return redirect('/login/')
	return check_login
