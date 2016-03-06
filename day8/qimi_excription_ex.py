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

try:
	# 抛异常
	raise qimiException("qimi的异常")
except qimiException as e:
	print(e)


# 断言,用于确保条件成立，接下来的代码才能运行


def test(a):
	# 传入的参数a必须为int类型，才能进入到异常处理代码块，这里打印print一个start try...做标记
	assert type(a) == int
	try:
		print("start try...")
		# 此处断言a == 1，如果不是就会抛出一个AssertionError
		assert a == 1
		print("yes!")
	# 捕获到断言抛出异常的话，就打印a的值
	except AssertionError:
		print("a = {}".format(a))

# 给test方法传一个非1的int
test(2)

