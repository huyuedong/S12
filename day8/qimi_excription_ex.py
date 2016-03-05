#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
自定义异常， 多用于业务类型异常，方便自己排查
"""


# 定义一个自己的异常类
class qimiException(Exception):
	def __init__(self, msg):
		self.msg = msg

	def __str__(self):
		return self.msg

a = 1
assert a == 1

try:
	raise qimiException("a != 2")
except qimiException as e:
	print(e)

