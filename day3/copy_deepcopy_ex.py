#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
深浅copy的区别
"""

import copy
# 数字、字符串
n1 = 123123
n2 = n1
print(id(n1))
print(id(n2))

n11 = '123123'
n22 = n11
print(id(n11))
print(id(n22))

print("浅copy".center(30, '*'))
n3 = copy.copy(n1)
print(id(n1))
print(id(n3))

print("深copy".center(30, '*'))
n4 = copy.deepcopy(n1)
print(id(n1))
print(id(n4))

# 其他
m1 = {'k1': 123, 'k2': '123', 'k3': [1, 3, 5]}
m2 = m1
print(id(m1))
print(id(m2))

print("浅copy".center(30, '*'))
m3 = copy.copy(m1)
print(id(m1))
print(id(m3))
print(id(m3['k3']))
print(id(m3['k3']))

print("深copy".center(30, '*'))
m4 = copy.deepcopy(m1)
print(id(m1))
print(id(m4))
print(id(m1['k3']))
print(id(m4['k3']))


# 应用
print('浅copy'.center(30, '*'))
old_dic = {'cpu': [80, ], 'disk': [70], 'memory': [60]}
# 浅copy之后，更改新字典的话，新旧字典一起更改
new_dic = copy.copy(old_dic)
new_dic['cpu'][0] = 50

print(old_dic)
print(new_dic)


print('深copy'.center(30, '*'))
old_dic2 = {'cpu': [80, ], 'disk': [70], 'memory': [60]}
# 深copy之后，更改新字典的话，新字典的值改变而旧字典的值不会变
new_dic2 = copy.deepcopy(old_dic2)
new_dic2['cpu'][0] = 50

print(old_dic2)
print(new_dic2)
