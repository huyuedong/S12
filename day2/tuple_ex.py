#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
元祖的元素不可变
元祖的元素的元素可以变
"""

t1 = (1, 2, {'k1': 'v1'})

t1[2]['k1'] = 2
print(t1)

print(t1[2])
