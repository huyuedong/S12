#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
游戏中的角色模型
名字，性别，体力值，精力值，资产，金钱，信心值
"""

from . import db_handler
from . import compute_value


# 定义一个总的角色类
class Role(object):
	def __init__(self, name, age, gender):
		self.name = name
		self.name = age
		self.gender = gender


# 定义一个boss类
class Boss(Role):
	def __init__(self, name, age, gender, asset, generous):
		super(Boss, self).__init__(name, age, gender)
		# 定义boss的资产
		self.asset = asset
		# 定义boss的康凯程度
		self.generous = generous


# 定义一个老师类
class Teacher(Role):
	def __init__(self, name, age, gender, ability, humor, price):
		super(Teacher, self).__init__(name, age, gender)
		# 定义老师的能力值
		self.ability = ability
		# 定义老师的幽默值
		self.humor = humor
		# 定义老师要收的学费
		self.price = price


# 定义一个玩家的类
class Player(Role):
	def __init__(self, name, age, gender, power, energy, money, confidence):
		super(Player, self).__init__(name, age, gender)
		self.power = power
		self.energy = energy
		self.money = money
		self.confidence = confidence

	def to_sleep(self, energy, hour):
		"""
		睡觉消耗时间，恢复精力值
		:param energy:
		:param hour:
		:return:
		"""
		print("{} will sleep {} hours.".format(self.name, hour))
		self.energy += energy

	def to_eat(self, power, food):
		"""
		消耗食物，增加力量值
		:param power: 力量值
		:param food: 食物类型
		:return:
		"""
		print("{} is eating {}.".format(self.name, food))
		self.power += power
