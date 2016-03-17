#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
如果线程打算一遍又一遍地重复通知某个事件，那最好使用Condition对象来处理。
实现一个周期性的定时器，每当定时器超时时，其他线程都可以感知到超时事件。
"""

import threading
import time


class PeriodicTimer(object):
	def __init__(self, interval):
		self._interval = interval
		self._flag = 0
		self._cv = threading.Condition()

	def start(self):
		t = threading.Thread(target=self.run)
		t.daemon = True
		t.start()

	def run(self):
		while True:
			time.sleep(self._interval)
			with self._cv:
				self._flag ^= 1
				# 唤起一个挂起的线程
				self._cv.notify_all()

	def wait_for_tick(self):
		"""
		wait for the next tick os the timer
		:return:
		"""
		with self._cv:
			last_flag = self._flag
			while last_flag == self._flag:
				# 挂起线程
				self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(5)
ptimer.start()


# Two threads that synchronize on the timer
def countdown(nticks):
	while nticks > 0:
		ptimer.wait_for_tick()
		print("T-minus", nticks)
		nticks -= 1


def countup(last):
	n = 0
	while n < last:
		ptimer.wait_for_tick()
		print('Counting', n)
		n += 1

threading.Thread(target=countdown, args=(10, )).start()
threading.Thread(target=countup, args=(5, )).start()

