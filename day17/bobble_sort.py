#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
冒泡排序
"""

import random
import time


def get_list(arg):
	"""
	获得一个有指定个数的1000以内数字的列表
	:param arg: 期望获得的列表内数字的个数
	:return:
	"""
	list_tmp = []
	for i in range(arg):
		list_tmp.append(random.randrange(100000))
	return list_tmp


def bubble_sort(arg):
	n = 0
	for i in range(len(arg)-1):
		n += 1
		for j in range(i+1, len(arg)):
			n += 1
			if arg[i] < arg[j]:
				arg[i], arg[j] = arg[j], arg[i]
	print("此次循环：{} 次。".format(n))
	return arg


if __name__ == "__main__":
	l1 = get_list(50000)
	start_time = time.time()
	l2 = bubble_sort(l1)
	end_time = time.time()
	print("此次耗时：{} 秒。".format(end_time-start_time))
