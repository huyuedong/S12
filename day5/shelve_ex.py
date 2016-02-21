#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
shelve模块
与pickle的不同是：pickle dump多次，然后按顺序load多次。
shelve打开一次就可以按照key来读取
"""

import shelve


# 定义一个测试类
class TestDemo(object):
	def __init__(self, n):
		self.n = n

t = TestDemo(123)

name = ["alex", "john", "eric"]

d = shelve.open("test3")

d["test1"] = name   # 持久化列表
d["test2"] = {"a": 1, "b": 2, "c": 3}   # 持久化列表
d["test3"] = t  # 持久化类实例

d.close()

p = shelve.open("test3")
print(p["test1"])
temp = p.get("test3")
print(temp.n)
p.close()
