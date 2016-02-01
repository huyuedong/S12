#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
shelve模块
"""

import shelve

d = shelve.open("test3.txt")


# 定义一个测试类
class TestDemo(object):
	def __init__(self, n):
		self.n = n

t = TestDemo(123)

name = ["alex", "john", "eric"]

d["test1"] = name   # 持久化列表
d["test2"] = t  # 持久化列表

d.close()

