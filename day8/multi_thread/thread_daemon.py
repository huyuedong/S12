#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
join、Daemon
"""

import time
import threading


def run(n):
	print("=========>{} running...".format(n))
	time.sleep(2)
	print("{} done...<=========".format(n))


def main():
	for i in range(5):
		t = threading.Thread(target=run, args=[i, ])
		t.start()
		t.join(1)
		print("Start thread:{}".format(t.getName()))

m = threading.Thread(target=main)
# m.setDaemon(True)
m.start()
m.join(timeout=2)
print("=======main thread done========")
