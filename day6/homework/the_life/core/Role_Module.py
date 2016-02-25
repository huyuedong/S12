#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
游戏中的角色模型
名字，性别，体力值，精力值，资产，金钱，信心值
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from core import db_handler
from core import compute_value


# 定义一个总的角色类
class Role(object):
	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	# 设置属性值
	def set_attr(self, key, value):
		object.__setattr__(self, key, value)

	# 获取属性值
	def get_attr(self, key):
		try:
			return object.__getattribute__(self, key)
		except:
			return "{} 没有找到！".format(key)

	# 说话
	def say(self, content, action=''):
		print("{} {} 说：{}".format(self.name, action, content))

	# 想
	def think(self, content):
		print("{} 心想：{}".format(self.name, content))


# 定义一个boss类
class Boss(Role):
	def __init__(self, name, age, gender, asset, generous):
		super(Boss, self).__init__(name, age, gender)
		# 定义boss的资产
		self.asset = asset
		# 定义boss的慷慨程度
		self.generous = generous


# 定义一个老师类
class Teacher(Role):
	def __init__(self, name, age, gender, course, tuition):
		super(Teacher, self).__init__(name, age, gender)

		# 定义老师教的科目
		self.course = course
		# 定义老师要收的学费
		self.tuition = tuition

	# 收取学费
	def take_tuition(self):
		print("收取学费{:.2f} 元。".format(self.tuition))

	# 教授知识
	def teaching(self, hours):
		print("{} 正在教你 {}...".format(self.name, self.course))
		print("{} 小时过后...".format(hours))


# 定义一个玩家的类
class Player(Role):
	def __init__(self, name, age, gender, power, energy, money, confidence):
		super(Player, self).__init__(name, age, gender)
		self.power = power
		self.energy = energy
		self.money = money
		self.confidence = confidence

	# 睡觉
	def to_sleep(self, hour):
		"""
		睡觉消耗时间，恢复精力值
		:param hour:
		:return:
		"""
		print("{} 要睡 {} 小时。".format(self.name, hour))
		print("{} 小时过去了... ")

	# 吃饭
	def to_eat(self, food):
		"""
		消耗食物，增加力量值
		:param food: 食物类型
		:return:
		"""
		print("{} 正在吃 {}.".format(self.name, food))
		print("{} 吃完了...")

	def learn(self, course, days=1):
		"""
		学习知识，按天增加自信心值
		:param course: 学的科目
		:param days: 学习时间
		:return:
		"""
		print("{} 正在学习 {}。".format(self.name, course))
		print("{} 小时过去了。。。".format(days))

	# 工作
	def work(self, days=1):
		"""
		工作， 按天取得报酬
		:param days: 工作时间
		:return:
		"""
		print("{} 工作了 {} 天。".format(self.name, days))
		print("{} 过去了。。。".format(days))

	# 消费
	def consume(self, goods, money):
		"""
		花钱，买东西
		:param goods: 物品名
		:param money: 钱的数量
		:return:
		"""
		print("{} 花了 {:.2f} 元买了 {}。".format(self.name, money, goods))

# a = Teacher("alex", 18, "male", "Python", 10000)
# b = Player("alex", 18, "male", 100, 100, 50, 50)
# print(b.confidence)
# print(b.get_attr("confidence"))
# b = compute_value.compute_value(b, "learn", 8)
# print(b.confidence)




