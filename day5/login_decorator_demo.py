#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
使用装饰器实现购物商城登录功能的demo
"""


def login(func):
	def inner():
		a = input("==>")
		if a == "1":
			func()
		else:
			print("...")
			pass
	return inner


@login
def main():
	print("购物商城主体")

if __name__ == "__main__":
	main()
