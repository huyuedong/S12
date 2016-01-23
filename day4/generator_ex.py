#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
生成器的练习
"""


def catch_mony(amount):
	while amount > 0:
		amount -= 100
		print("又来取钱了！")
		yield "给你100吧。。。"

atm = catch_mony(500)
print(type(atm))
print(atm.__next__())
print(atm.__next__())
print("去看电影！。。。")
print(atm.__next__())


