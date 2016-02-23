#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
大家都知道计算机最终是使用二进制存储（也就是 0 1 ），那么现在来请大家帮我分别算出 "武沛齐" 和 "wupeiqi"   两个字符串的二进制表示。
这个2进制的表示请以列表的形式打印出来， 意思就是:如果二进制结果是01110， 那用列表的表示就是[2，3，4]，就是，第几个bit的位置是1，
就在列表中依次写上这个bit的位置
"""
from collections import defaultdict
str1 = "武沛齐"
str2 = "wupeiqi"

# l1 = []
# l2 = []
# for i in str2:
# 	print(bin(ord(i)).replace("0b", ""))
# 	temp = bin(ord(i)).replace("0b", "")
# 	l1.append(temp)
# 	# for j in temp:
# 	# 	print(j)
# 	# 	if j == "1":
# 	# 		print("{}:{}".format(temp, temp.index(j)))
# print(l1)
# str3 = '1110111'
# index_list = []
# for i in range(len(str3)):
# 	if str3[i] == "1":
# 		print("{}:{}".format(str3, i))
# 		index_list.append(i)
# print(index_list)


# 获取字符串中1的下标
def get_index(arg):
	"""

	:param arg: 传入的字符串参数
	:return: 字符串的二进制表示及其第几bit位是1
	"""
	index_dic = defaultdict(dict)   # 定义一个字典用于存放结果，格式为字符串：二进制数：1的bit位
	for i in arg:
		bin_str = bin(ord(i)).replace('0b', '')    # 二进制
		index_dic[i] = defaultdict(list)    # 定义一个字典，键：二进制数，值：1的bit位
		for j in range(len(bin_str)):
			if bin_str[j] == "1":
				index_dic[i][bin_str].append(j+1)
	return index_dic

a = get_index(str1)
for k1 in a:
	for k2 in a[k1]:
		print("{}的二进制数字是：{}，其中是1的bit位是：{}".format(k1, k2, a[k1][k2]))
