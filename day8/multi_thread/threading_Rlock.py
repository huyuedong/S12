#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
RLock,递归锁，也就是大锁里面包含小锁
"""

import threading


def run1():
	# 小锁1
	lock.acquire()
	global num1
	num1 += 1
	lock.release()
	return num1


def run2():
	# 小锁2
	lock.acquire()
	global num2
	num2 += 1
	lock.release()
	return num2


def run():
	# 大锁
	lock.acquire()
	result1 = run1()
	print("===-between run1 and run2-===")
	result2 = run2()
	print("result1:{}, result2:{}".format(result1, result2))
	lock.release()


if __name__ == "__main__":

	num1, num2 = 0, 0
	lock = threading.RLock()
	for i in range(3):
		t = threading.Thread(target=run)
		t.start()
		t.join()

	while threading.active_count() != 1:
		print(threading.active_count())
	else:
		print("======-all threading done!-======")
		print("num1:{},num2:{}".format(num1, num2))


