#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
生产者消费者模型
代码中写了两个类，Consumer和Producer，分别继承了Thread类，我们分别初始化这两个类获得了c和p对象，并启动这两个线程。
则这两个线程去执行run方法（这里与Thread类内部的调度有关），定义了producer全局变量和condition对象为全局变量，
当producer不大于1时，消费者线程被condition对象阻塞，不能继续消费（这里是不再递减），
当producer不小于10时，生产者线程被condition对象阻塞，不再生产（这里是不再累加）。
"""

import threading
import time


condition = threading.Condition()
products = 0


class Producer(threading.Thread):
	def __init__(self):
		super(Producer, self).__init__()

	def run(self):
		global condition, products
		while True:
			if condition.acquire():
				if products < 10:
					products += 1
					print("Producer:{} deliver one, now products:{}.".format(self.name, products))
					condition.notify()      # 唤醒一个挂起的线程，这里就是喊人来消费
				else:
					print("Producer:{} already 10, stop deliver, now products:{}.".format(self.name, products))
					condition.wait()    # 释放线程锁，并挂起线程。
				condition.release()
				time.sleep(2)


class Consumer(threading.Thread):
	def __init__(self):
		super(Consumer, self).__init__()

	def run(self):
		global condition, products
		while True:
			if condition.acquire():
				if products > 1:
					products -= 1
					print("Consumer:{} consume one, now products:{}".format(self.name, products))
					condition.notify()      # 唤醒一个挂起的线程。
				else:
					print("Cousumer:{} only one, stop consume, now products:{}".format(self.name, products))
					condition.wait()    # 释放线程锁，并挂起线程。
				condition.release()
				time.sleep(2)


if __name__ == "__main__":
	for p in range(2):
		p = Producer()
		p.start()

	for c in range(10):
		c = Consumer()
		c.start()
