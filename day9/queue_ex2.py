#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
queue的生产者消费者模型

"""

import queue
import time
import threading


q = queue.Queue()
num = 0


def producer(name, num):
	while True:
		print("cook:{} product baozi:{}.".format(name, num))
		q.put(num)
		num += 1
		q.join()    # 阻塞中，等待信号,q.empty()触发，这里相当于发广播，所有的线程都会受到这个触发。
		print("all baozi has been eating...")


def consumer(name):
	while True:
		data = q.get()
		print("name:{} eat baozi:{}.".format(name, data))
		time.sleep(1)
		q.task_done()   # 告诉q完成任务


p1 = threading.Thread(target=producer, args=("A", num))
p2 = threading.Thread(target=producer, args=("B", num))
c1 = threading.Thread(target=consumer, args=("22",))
c2 = threading.Thread(target=consumer, args=("23",))
p1.start()
p2.start()
c1.start()
c2.start()
