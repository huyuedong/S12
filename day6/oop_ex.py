#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
类似CS的小游戏
"""


# 角色基类
class Role(object):
	# 类属性
	count = 0
	
	def __init__(self, name, role, weapon, life_value):
		self.name = name
		self.role = role
		self.weapon = weapon
		self.life_value = life_value
		Role.count += 1

	def buy_weapon(self, weapon):
		"""

		:type weapon: object
		"""
		print("{} buy {}".format(self.name, weapon))
		self.weapon = weapon

# 实例化一个角色
# 把一个抽象的类变成一个具体的实例的过程，叫做实例化。
p1 = Role("alex", "police", "Knife", 100)
t1 = Role("john", "terrorist", "Knife", 100)
print(p1.name)

# 买枪
p1.buy_weapon("M4A1")
t1.buy_weapon("AK47")

# print(p1.weapon)
# print(t1.weapon)
# print(Role.count)
