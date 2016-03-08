#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
进程池
"""

from multiprocessing import Pool, freeze_support
import time


def func1(i):
	time.sleep(1)
	return i + 100


def func2(arg):
	print("==> exec done:", arg)

if __name__ == "__main__":
	freeze_support()
	# 定义一个数量为5的进程池
	pool = Pool(5)
	for i in range(10):
		# 异步，将func1的返回值传给func2
		pool.apply_async(func1, args=(i,), callback=func2)
		# 同步，没有callback时
		# result = pool.apply(func=func1, args=(i,))
	print("=====-end-=====")
	pool.close()
	pool.join()     # 进程池中进程执行完毕后再关闭，如果不写，那么程序直接关闭


