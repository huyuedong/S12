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

	@classmethod    # 类方法，不能访问实例变量
	def talk(cls):
		print(" is talking.")

	@staticmethod   # 静态方法，不能访问类变量及实例变量
	def walk():
		print("{} is walking.")

	@property   # 把方法变成属性
	def habit(self):
		return "{} habit is eating.".format(self.name)

	@property
	def total_players(self):
		return self.num

	@total_players.setter
	def total_players(self, num):
		self.num = num
		print("total players: {}".format(self.num))

	@total_players.deleter
	def total_players(self):
		del self.num
		print("total players is deleted.")

# 访问habit属性
a = Animal("tommie")
# 调用时不需要加括号
s = a.habit
print(s)
