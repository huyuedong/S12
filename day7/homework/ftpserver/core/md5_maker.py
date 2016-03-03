#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
生成文件的md5值
"""

import hashlib
import os


def md5_maker(arg):
	m = hashlib.md5()
	# 判断传入的参数路径是不是一个文件
	if os.path.isfile(arg):
		# 以二进制打开一个文件对象
		with open(arg, "rb") as f:
			# 一次读取1024
			bytes_data = f.read(1024)
			# 循环读取，并生成md5加密串
			while bytes_data != b"":
				m.update(bytes_data)
				bytes_data = f.read(1024)
			else:
				return m.hexdigest()
	else:
		return None
