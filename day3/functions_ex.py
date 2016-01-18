#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
自定义的函数
"""


# 无参数
def sho():
	print("无参数函数")

sho()


# 一个参数
# 注意：函数遇到return关键字就跳出了，所以下例中的print('b')并不会被执行
def show(a):
	print(a)
	return [11, 22]
	print('b')
result = show(333)
print(result)
print("分割线".center(30, '*'))


# 两个参数
def show0(a1, a2):
	print(a1)
	print(a2)
show0(111, 333)


# 默认参数
def show1(a1, a2=555):
	print(a1)
	print(a2)
show1(111)
show1(111, 333)
show1(a2=333, a1=111)


# *args即代表传入的参数按照列表或元祖处理
# 动态参数-元祖
def show2(*args):
	print(args, type(args))

show2(11, 22, 33, 44)


# 动态参数-列表
def show2(*args):
	print(args, type(args))

show2([11, 22, 33, 44])
l1 = [44, 55, 66, 77]
show2(* l1)
print('分割线-line:72'.center(30, '*'))


# **kwargs代表传入的参数按照字典来处理
# 动态参数-字典
def show3(**kwargs):
	print(kwargs, type(kwargs))

show3(n1=11, n2=22)


# 动态参数-序列和字典
def show4(*args, **kwargs):
	print(args, type(args))
	print(kwargs, type(kwargs))
show4(11, 22, 33, n=44, m=55)

# 注意：
l = [11, 22, 33]
d = {'n': 44, 'm': 55}
# 直接传入会把l和d,传入*args
show4(l, d)

# 需要对传入的参数进行处理
show4(*l, **d)


# 用于字符串的格式化
str_tmp = "{0} is {1}!"
result = str_tmp.format('alex', 'humor')
print(result)

result = str_tmp.format(*['alex', 'humor'])
print(result)

str_tmp = "{name} is {actor}!"
print(str_tmp.format(name='alex', actor='humor'))

d_tmp = {'name': 'alex', 'actor': 'humor'}
result = str_tmp.format(**d_tmp)
print(result)


# 简单函数lambda
def func_tmp(a):
	return a+1
result1 = func_tmp(99)
print(result1)
result2 = lambda a: a+1
print(result2(99))

