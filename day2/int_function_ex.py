#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
"""
int类的几个内建方法
"""
all_pages = 95
per_page = 10

pages = all_pages.__divmod__(per_page)
print(pages)

num1 = -19
print(abs(num1))
print(num1.__abs__())

num2 = 5
print(num1+num2)
print(num2.__add__(num1))

