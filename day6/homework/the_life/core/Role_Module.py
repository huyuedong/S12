#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
游戏中的角色模型
名字，性别，体力值，精力值，资产，金钱，信心值
"""


class Role(object):
	def __init__(self, name, gender, power, energy, asset, money, confidence):
		self.name = name
		self.gender = gender
		self.power = power
		self.energy = energy
		self.asset = asset
		self.money = money
		self.confidence = confidence

	def to_sleep(self, name, energy, hour):
		"""
		睡觉消耗时间，恢复精力值
		:param name:
		:param energy:
		:param hour:
		:return:
		"""
		print("{} will sleep {} hours.".format(name, hour))
		assert isinstance(self.energy, int)
		self.energy += energy

	def to_eat(self, name, power, food):
		"""
		吃饭消耗食物，恢复体力值
		:return:
		"""
		print("{} is eating {}.".format(name, food))
		self.power += power

