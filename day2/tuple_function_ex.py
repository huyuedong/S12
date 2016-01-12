#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
tuple的内建方法
* -元祖的元素不可变
* -元祖的元素的元素可以变
"""

# 计数
t1 = (1, 1, 2, 3, 4, 4, 1)
print(t1.count(1))

# 索引
print(t1.index(2))

print('line:18'.center(20, '='))

t1 = (1, 2, {'k1': 'v1'})
t1[2]['k1'] = 2
print(t1)
print(t1[2])
