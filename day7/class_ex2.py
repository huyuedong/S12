#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
"""
经典类和新式类的区别
经典类是深度优先，新式类是广度优先
Python3.0修复了这个问题，无论是经典类还是新式类都是广度优先
"""


class A:
	n = "A"

	def f2(self):
		print("f1 from A")


class B(A):
	n = "B"

	def f1(self):
		print("f1 from B")

	def f2(self):
		print("f2 from B")


class C(A):
	n = "C"

	def f1(self):
		print("f1 from C")


# 多继承
class D(B, C):
	pass

# 实例化一个D类
d = D()
# 默认（先在同级别从左往右）即：从B类找f1，找不到就去同级别的A类去找，找不到就往上一级去找f1
d.f1()
d.f2()

