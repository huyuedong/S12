#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
多进程的Queue
"""

from multiprocessing import Process, Queue


def func(q):
	q.put(["alex", 18, "Girls"])


if __name__ == "__main__":
	que = Queue()
	p1 = Process(target=func, args=(que,))
	p2 = Process(target=func, args=(que,))

	p1.start()
	p2.start()

	print("from parent p1:", que.get())
	print("from parent p2:", que.get())

	p1.join()
	p2.join()
