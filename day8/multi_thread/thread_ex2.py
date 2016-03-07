#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
继承的方式起线程
"""

import threading
import time


# 定义一个线程类
class MyThread(threading.Thread):

	def __init__(self, num):
		super(MyThread, self).__init__()
		self.num = num

	def run(self):
		print("Running num:{}".format(self.num))
		time.sleep(3)

if __name__ == "__main__":
	t1 = MyThread(1)
	t2 = MyThread(2)

	t1.start()
	t2.start()

	print("=======main==========")

	print(t1.getName())
	print(t2.getName())
