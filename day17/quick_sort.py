#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import random
import time

"""
快速排序
"""


def get_list(arg):
	"""
	获得一个有指定个数的1000以内数字的列表
	:param arg: 期望获得的列表内数字的个数
	:return:
	"""
	list_tmp = []
	for i in range(arg):
		list_tmp.append(random.randrange(10))
	return list_tmp


def quick_sort(original_list, start, end):
	print(start, end)
	"""

	:param original_list: 待排序的列表
	:param left: 第一个元素的索引
	:param right: 最后一个元素的索引
	:return:
	"""
	# 参数输错直接退出
	if start >= end:
		return
	# 取一个key值
	value_key = original_list[start]

	left = start
	right = end

	while left < right:
		# 先从右往左比较
		while left < right and original_list[right] > value_key:
			right -= 1
		# 把最前面的值跟这个比key小的值互换
		# 把最左边的值换成从右往左找到的那个比key小的那个值
		original_list[left], original_list[right] = original_list[right], original_list[left]
		#
		while left < right and original_list[left] <= value_key:
			left += 1
		# 如果从左往右找到了比key大的数
		original_list[left], original_list[right] = original_list[right], original_list[left]
	quick_sort(original_list, start, left-1)
	quick_sort(original_list, right+1, end)


if __name__ == "__main__":
	l1 = get_list(6)
	print(l1)
	start_time = time.time()
	quick_sort(l1, 0, len(l1)-1)
	end_time = time.time()
	print("此次耗时：{} 秒。".format(end_time-start_time))
	print(l1)
