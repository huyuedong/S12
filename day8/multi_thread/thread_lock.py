#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
线程锁，区别于GIL
"""

import threading
import time


def minus_num():
	global num  # 因为在函数里面要对num进行修改，所以必须声明num为全局变量
	# 获取线程锁
	lock.acquire()  # 因为在函数里只是对lock进行访问，不涉及到修改，所以无需在开头声明lock为全局变量
	print("get num=>{}".format(num))
	# time.sleep(1)
	num -= 1
	print("the result=>{}".format(num))
	# 释放线程锁
	lock.release()


lock = threading.Lock()     # 生成一个线程锁实例(全局锁)
num = 100   # 设置一个共享变量

thread_list = []
for i in range(100):
	t = threading.Thread(target=minus_num)
	t.start()
	thread_list.append(t)

# 等到所有的子线程都结束
for j in thread_list:
	j.join()

print("final num:{}".format(num))
