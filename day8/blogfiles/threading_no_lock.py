#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
没有加锁的多线程处理同一个数据
"""

import threading
import time


def minus_num():
	global num
	print("get the num:", num)
	# time.sleep(1)
	num -= 1
	print("The result:", num)


if __name__ == "__main__":
	num = 100
	lock = threading.Lock()

	thread_list = []
	for i in range(100):
		t = threading.Thread(target=minus_num)
		t.start()
		thread_list.append(t)

	for j in thread_list:
		j.join()

	print("The result=>:", num)
