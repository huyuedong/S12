#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
信号量
互斥锁同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据。
如果线程数超过了定义的值，就要等待一个线程结束之后，再进行下一个。
"""

import threading
import time


def run(n):
	semaphore.acquire()
	time.sleep(1)
	print("run the thread:{}\n".format(n))
	semaphore.release()

if __name__ == "__main__":
	num = 0
	semaphore = threading.BoundedSemaphore(5)   # 最多允许5个线程同时启动
	for i in range(20):
		t = threading.Thread(target=run, args=(i,))
		t.start()

	while threading.active_count() != 1:
		# print("there are {} threads.".format(threading.active_count()))
		pass
	else:
		print("=====-all threads done-=====")
		print(num)

