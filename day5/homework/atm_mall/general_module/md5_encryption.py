#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
加密算法
"""

import hashlib


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

