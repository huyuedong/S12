#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
shelve模块
"""

import shelve
import pickle

# d = shelve.open("test3")
#
#
# # 定义一个测试类
# class TestDemo(object):
# 	def __init__(self, n):
# 		self.n = n
#
# t = TestDemo(123)
#
# name = ["alex", "john", "eric"]
#
# d["test1"] = name   # 持久化列表
# d["test2"] = {"a": 1, "b": 2, "c": 3}   # 持久化列表
# d["test3"] = t  # 持久化类实例
#
# d.close()

p = shelve.open("test3")
for i in p.keys():
	print(i)
	print(p[i])
p.close()
