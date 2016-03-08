#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
进程同步：加锁
"""

from multiprocessing import Process, Lock


# def func(l, i):
# 	l.acquire()
# 	try:
# 		print("Hello world:", i)
# 	finally:
# 		l.release()
#
# if __name__ == "__main__":
# 	lock = Lock()
#
# 	for num in range(10):
# 		Process(target=func, args=(lock, num)).start()


def func(i):
	print("Hello world:", i)

if __name__ == "__main__":
	lock = Lock()

	for num in range(10):
		Process(target=func, args=(num,)).start()
