#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
join、Daemon
守护线程结束时会自动关闭子线程
join被设置timeout参数时会等待指定的时间，否则就等待到程序完成
"""

import time
import threading


# 定义一个所有线程都要运行的函数
def run(n):
	print("=========>{} running...".format(n))
	time.sleep(2)
	print("{} done...<=========".format(n))


def main():
	for i in range(5):
		t = threading.Thread(target=run, args=[i, ])
		t.start()
		t.join()
		print("Start thread:{}".format(t.getName()))

m = threading.Thread(target=main)
m.setDaemon(True)     # 将主线程设置为Daemon线程,它退出时,其它子线程会同时退出,不管是否执行完任务
m.start()
m.join()
print("=======main thread done========")
