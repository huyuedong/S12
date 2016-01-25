#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


"""
递归的练习
"""


# def calc(n):
# 	print(n)
# 	if n / 2 > 1:
# 		res = calc(n/2)
# 		print("res:{}".format(res))
# 	print("n:{}".format(n))
# 	return n

# calc(10)


# 斐波那契数列练习
# def func(arg1, arg2, stop):
# 	if arg1 == 0:
# 		print(arg1)
# 		print(arg2)
# 	arg3 = arg1 + arg2
# 	if arg3 < stop:
# 		print(arg3)
# 		func(arg2, arg3, stop)

# func(0, 1, 30)


# 二分法查找find_num在不在data_base中：
# def binary_search(data_base, find_num):
# 	mid = int(len(data_base)/2)
# 	if len(data_base) > 1:
# 		if data_base[mid] > find_num:
# 			binary_search(data_base[:mid], find_num)
# 		elif data_base[mid] < find_num:
# 			binary_search(data_base[mid:], find_num)
# 		else:
# 			print("找到了！")
# 	elif len(data_base) == 1:
# 		if data_base[0] == find_num:
# 			print("找到了！")
# 		else:
# 			print("没找到！")
# 	else:
# 		print("没找到！")
#
# da_base = list(range(0, 10000000, 4))
# binary_search(da_base, 2)


# 汉诺塔游戏
# n:A柱上有多少个盘子，a:左边的柱子，b:中间的柱子，c:右边的柱子
# 把左边柱子上的n个盘子移动到右边的柱子的详细步骤，盘子分大小，小盘子只能放在比他大的盘子上。
# def mov_h(n, a, b, c):
# 	if n == 1:
# 		print("{}==>{}".format(a, c))
# 	elif n > 1:
# 		mov_h(n-1, a, c, b)
# 		mov_h(1, a, b, c)
# 		mov_h(n-1, b, a, c)
# 	else:
# 		print("参数错误！")
#
# mov_h(5, 'A', 'B', 'C')


# 打印一个二维数组：
list_demo = [[i for i in range(4)] for i in range(4)]


def show(arg):
	for i in arg:
		print(i)

# 顺时针转90度
# for i in range(len(list_demo)):
# 	for j in range(i, len(list_demo)):
# 		list_demo[i][j], list_demo[j][i] = list_demo[j][i], list_demo[i][j]


# 逆时针转90度
# for i in range(len(list_demo)).__reversed__():
# 	print(list_demo[i])

# show(list_demo)

# 打印9*9乘法表
for i in range(1, 10):
	for j in range(1, i):
		print("{}*{}={}\t".format(j, i, i*j).lstrip(), end=" ")
	if i == 1:  # 要不然第一行和其他行对不齐。。。
		print(" {}*{}={}\n".format(i, i, i*i), end=" ")
	else:
		print("{}*{}={}\n".format(i, i, i*i), end=" ")

# 另外一种方法，但是两行之间多了空行
# for i in range(1, 10):
# 	for j in range(1, i+1):
# 		print("{}*{}={}".format(j, i, i*j), end=" ")
# 	print("\n")
