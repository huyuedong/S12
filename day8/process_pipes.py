#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
进程间通信的一种方法：pipes
"""

from multiprocessing import Process, Pipe


def func(conn):
	conn.send(["alex", 18, "Girls"])


if __name__ == "__main__":
	# 父发，子收
	parent_conn, child_conn = Pipe()
	p1 = Process(target=func, args=(parent_conn,))
	p2 = Process(target=func, args=(parent_conn,))

	p1.start()
	p2.start()

	print("from parent p1:", child_conn.recv())
	print("from parent p2:", child_conn.recv())

	p1.join()
	p2.join()
