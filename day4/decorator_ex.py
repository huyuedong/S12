#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
装饰器的练习
"""


# def login(func):
# 	print("这是验证功能。。。")
# 	return func
#
#
# def home():
# 	print("This is the Home page.")
#
#
# def tv():
# 	print("This is the TV page")
#
# # 需求是在访问tv页面之前加上验证功能。
# tv = login(tv)
# tv()
# 这样可以实现需求，但是把tv函数改变了，而且当login函数需要传入参数的时候，就不好处理了。


# 下面是使用装饰器来实现：
# def login(func):
# 	def inner():
# 		print("正在验证！。。。")
# 		func()
# 		print("welcome to the tv page!")
# 	return inner


# @login
# def tv():
# 	print("This is  the tv page!")
#
# tv()
#

# 被装饰的函数需要参数时：
# def login(func):
# 	def inner(*args):
# 		print("正在验证！。。。")
# 		func(*args)
# 		print("Have a nice time!")
# 	return inner
#
#
# @login
# def movie(*args):
# 	print("welcome {} to the {} page of movie!".format(*args))
#
# movie("Alex", '3rd')


# 当被装饰的函数有返回值时：
# def login(func):
# 	def inner(*args):
# 		print("正在验证！。。。")
# 		tmp = func(*args)
# 		print("Have a nice time!")
# 		return tmp  # 注意：此处应该将被装饰函数的返回值return
# 	return inner
#
#
# @login
# def movie(*args):
# 	print("welcome {} to the {} page of movie!".format(*args))
# 	return 666  # 被装饰的函数有返回值
#
# num = movie("Alex", '3rd')
# print(num)


# 复杂的装饰器：
def login():
	print("开始进行验证。。。")


def errorhandle():
	print("出错啦。。。")


# 给装饰器加参数 复杂的装饰器
def f(before_func, after_func):    # 第一层传入装饰器的参数
	def outer(main_func):   # 第二层传入被装饰的函数名
		def inner(*args):    # 第三层传入被装饰函数的参数
			before_func()
			main_func(*args)
			after_func()
		return inner
	return outer


@f(login, errorhandle)
def index(name):
	print("{}:这是主程序。".format(name))


index('alex')


# def login():
# 	print("开始进行验证。。。")
#
#
# def errorhandle():
# 	print("出错啦。。。")
#
#
# # 给装饰器加参数 复杂的装饰器
# def f(arg):
# 	def outer(main_func):
# 		def inner():
# 			arg()
# 			main_func()
# 		return inner
# 	return outer
#
#
# @f(errorhandle)
# # @f(login)   # 给装饰器传入不同的函数，被装饰的函数就扩展了不同的功能。
# def index():
# 	print("这是主程序。")
#
#
# index()
