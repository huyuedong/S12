#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
类的进阶练习
"""


class Animal(object):
	def __init__(self, name):
		self.name = name
		self.num = None

	def say_hi(self):   # 普通方法，由实例调用访问实例变量
		print("Hi~ {}".format(self.name))

	@classmethod    # 类方法，不能访问实例变量
	def talk(cls):
		print(" is talking.")

	@staticmethod   # 静态方法，不能访问类变量及实例变量
	def walk():
		print("{} is walking.")

	@property   # 把方法变成属性，可以调用实例变量
	def habit(self):
		return "{}'s habit is eating.".format(self.name)

	@property   # 定义类属性
	def total_animals(self):
		return self.num

	@total_animals.setter   # 给类属性赋值
	def total_animals(self, num):
		self.num = num
		print("total animals: {}".format(self.num))

	@total_animals.deleter  # 删除类属性
	def total_animals(self):
		del self.num
		print("total animals is deleted.")

# 访问habit属性
a = Animal("tommie")

# 调用时不需要加括号
print(a.habit)
a.say_hi()

# 打印类属性
print(a.total_animals)

# 给类属性赋值
a.total_animals = 10
print(a.total_animals)

# 删除类属性
del a.total_animals
try:
	print(a.total_animals)
except AttributeError as e:
	print(e)

