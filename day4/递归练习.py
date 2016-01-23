#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


"""
递归的练习
"""


def calc(n):
	print(n)
	if n / 2 > 1:
		res = calc(n/2)
		print("res:{}".format(res))
	print("n:{}".format(n))
	return n

# calc(10)


# 斐波那契数列练习
def func(arg1, arg2, stop):
	if arg1 == 0:
		print(arg1)
		print(arg2)
	arg3 = arg1 + arg2
	if arg3 < stop:
		print(arg3)
		func(arg2, arg3, stop)

# func(0, 1, 30)


# 二分法
def binary_search(data_base, find_num):
	if len(data_base) >= 1:
		mid = int(len(data_base)/2)
		if data_base[mid] > find_num:
			binary_search(data_base[:mid], find_num)
		elif data_base[mid] < find_num:
			binary_search(data_base[mid:], find_num)
		else:
			print("{}在{}中".format(find_num, 'data_base'))
	else:
		print("{}不在{}中".format(find_num, 'data_base'))

daba_base = list(range(100))
binary_search(daba_base, 0)

