#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
迭代器的列练习
"""

tmp = iter(['alex', 'jack', 'rain'])

print(tmp.__next__())
print(tmp.__next__())
print(tmp.__next__())
# print(tmp.__next__())   # 再取值就会报错，raise StopIteration

list_tmp = [1, 22, 333, 4444, 55555]
for i in iter(list_tmp):
	print(i)
