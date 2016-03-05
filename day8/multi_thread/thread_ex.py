#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
直接调用的多线程
"""

import threading
import time


# 定义一个每个线程要运行的函数
def sayhi(num):
	print("running number:{}".format(num))
	time.sleep(3)

if __name__ == "__main__":
	t1 = threading.Thread(target=sayhi, args=[1, ])     # 生成一个线程实例t1
	t2 = threading.Thread(target=sayhi, args=[2, ])     # 生成一个线程实例2

	t1.start()  # 启动线程t1
	t2.start()  # 启动线程t2

	print("========main===========")    # 主线程的print()
