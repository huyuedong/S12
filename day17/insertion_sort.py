#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import random
import time

"""
插入排序
"""


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


def insertion_sort(arg):
	n = 0
	for i in range(1, len(arg)):
		n += 1
		# 记下当前的索引
		index = i
		# 记下当前值
		current_value = arg[i]
		# 如果索引大于0，并且它前面已经排序了的列表的最后一个值比当前值大
		while index > 0 and arg[index-1] > current_value:
			# 就把它之前已经排序了的列表的值往后移一位
			arg[index] = arg[index-1]
			# 接着在已经排序的列表往前取值比较
			index -= 1
			n += 1
		# 如果索引=0或者当前的已经排序了的列表中索引为index-1的值比当前值小
		# 那么就把current_value放到index位置
		arg[index] = current_value
	print("此次循环：{} 次。".format(n))
	return arg


if __name__ == "__main__":
	l1 = get_list(50000)
	print(l1)
	start_time = time.time()
	l2 = insertion_sort(l1)
	end_time = time.time()
	print("此次耗时：{} 秒。".format(end_time-start_time))
	print(l2)
