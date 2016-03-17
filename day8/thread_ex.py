#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


"""
5个人吃5碗饭，只有5只筷子
"""

import threading
from contextlib import contextmanager

# Thread-local state 存储已经获取的锁信息
_local = threading.local()


@contextmanager
def acquire(*locks):
	# 将锁排序
	locks = sorted(locks, key=lambda x: id(x))
	# 确保之前的锁也是按顺序的
	acquired = getattr(_local, 'acquired', [])
	if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
		raise RuntimeError("Lock Order Violation.")
	# 获取所有的锁
	acquired.extend(locks)
	_local.acquired = acquired

	try:
		for lock in locks:
			lock.acquire()
		yield
	finally:
		# 按获取的反顺序释放所有的锁
		for lock in reversed(locks):
			lock.release()
		# 将locks都从acquired删除
		del acquired[-len(locks):]


# The human thread
def human(left, right):
	while True:
		with acquire(left, right):
			print(threading.currentThread(), "eating...")

# 筷子
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]


def main():
	for n in range(NSTICKS):
		t = threading.Thread(target=human, args=(chopsticks[n], chopsticks[(n+1) % NSTICKS]))
		t.start()

if __name__ == '__main__':
	main()
