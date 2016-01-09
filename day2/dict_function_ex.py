#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
dict内建的方法练习
"""

dic1 = {'k1': 'v1', 'k2': 'v2', }
print(dic1)
dic1 = dict(k1='v1', k2='v2')
print(dic1)

# fromkeys
dic2 = dict.fromkeys(['k1', 'k2', ], 1)
print(dic2)

# get()

# items()

# [11, 22, 33, 44, 55, 66, 77, 88, 99, ...]大于66的保存在字典的第一个key的值中，小于等于66的放到第二个key的值中
# {'key1':大于66的， 'key2':小于等于66的}

l1 = [11, 22, 33, 44, 55, 66, 77, 88, 90, 99, ]
dic = {}
for i in l1:
	if i > 66:
		if 'key1' in dic.keys():
			dic['key1'].append(i)
		else:
			dic['key1'] = [i, ]
	else:
		if 'key2' in dic.keys():
			dic['key2'].append(i)
		else:
			dic['key2'] = [i, ]
print(dic)
