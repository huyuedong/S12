#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
yield小练习
"""

import time


def consumer(name):
	print("{}准备吃包子啦！".format(name))
	while True:
		baozi = yield   # yield也可以用于接收值
		print("第{}次的包子来了，被{}吃掉了！".format(baozi, name))


def producer(name):
	c1 = consumer('A')
	c2 = consumer('B')
	c1.__next__()
	c2.__next__()
	print("{}准备开始做包子了！".format(name))
	for i in range(1, 11):
		time.sleep(1)
		print("{}第{}次做了两个包子。".format(name, i))
		c1.send(i)  # 将i的值传给yield
		c2.send(i)  # 将i的值传给yield

producer("老板")
