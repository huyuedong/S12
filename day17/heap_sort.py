#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
堆排序
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
		list_tmp.append(random.randrange(1000000))
	return list_tmp


def sift_down(lst, start, end):
	"""

	:param lst: 待排序的数组
	:param start: 开始排序的节点
	:param end: 末节点
	:return: 调整为最大堆结构
	"""
	root = start
	while True:
		child = 2 * root + 1  # 默认设置左子节点为最大子节点
		# 子节点越界就跳出
		if child > end:
			break
		# 如果右子节点没越界，并且右子节点的值比左子节点大
		if child + 1 <= end and lst[child] < lst[child+1]:
			# 设置右子节点为最大子节点
			child += 1
		# 如果根节点的数小于值大的那个子节点
		if lst[root] < lst[child]:
			# 互换位置
			lst[root], lst[child] = lst[child], lst[root]
			# 设置正在调整的节点为root
			root = child
		# 无需调整就退出
		else:
			break


def heap_sort(lst):
	for i in range(len(lst)//2, -1, -1):
		sift_down(lst, i, len(lst)-1)
	for j in range(len(lst)-1, 0, -1):
		lst[0], lst[j] = lst[j], lst[0]
		sift_down(lst, 0, j-1)
	return lst


if __name__ == "__main__":
	list_demo = get_list(500000)
	start_time = time.time()
	heap_sort(list_demo)
	end_time = time.time()
	print("此次耗时：{} 秒。".format(end_time-start_time))
