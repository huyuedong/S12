#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
装饰器的练习
"""


# def login(func):
# 	print("验证中。。。")
# 	return func
#
#
# def home():
# 	print("Home page.")
#
#
# def tv():
# 	print("TV page")
#
#
# tv = login(tv)
# tv()


# def login(func):
# 	def inner(*arg):
# 		print("正在验证！。。。")
# 		func(*arg)
# 	return inner
#
#
# @login
# def tv(name):
# 	print("welcome {} to the tv page!".format(name))
#
#
# @login
# def movie(*args):
# 	print("welcome {} to the {} page!".format(*args))
#
# tv("Alex")
# movie("Alex", 3)


def login():
	print("开始进行验证。。。")


def errorhandle():
	print("出错啦。。。")


# 给装饰器加参数 复杂的装饰器
def f(before_func, after_func):
	def outer(main_func):
		def wrapper():
			before_func()
			main_func()
			after_func()
		return wrapper
	return outer


@f(login, errorhandle)
def index():
	print("这是主程序。")


index()
