#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
event红绿灯的例子
"""

import threading
import time


def light():
	if not event.isSet():
		event.set()
	count = 0
	while True:
		if count < 10:
			print("\033[42;1m== green light on ==\033[0m")
		elif count < 13:
			print("\033[43;1m== yellow light on ==\033[0m")
		elif count < 20:
			if event.isSet():
				event.clear()
			print("\033[41;1m== red light on ==\033[0m")
		else:
			count = 0
			event.set()     # 打开绿灯
		time.sleep(1)
		count += 1


def car(n):     # no bug version
	while True:
		time.sleep(1)
		if event.isSet():
			print("car {} is running...".format(n))
		else:
			print("car {} is waiting for the red light...".format(n))
			event.wait()


if __name__ == "__main__":
	event = threading.Event()

	# 起一个线程模拟红绿灯
	Light = threading.Thread(target=light)
	Light.start()

	# 起三个线程模拟汽车
	for i in range(3):
		Car = threading.Thread(target=car, args=(i,))
		Car.start()
