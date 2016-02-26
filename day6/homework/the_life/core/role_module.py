#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
游戏中的角色模型
名字，性别，体力值，精力值，资产，金钱，信心值
"""

import os
import sys
import time
from collections import OrderedDict
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from core import db_handler
from core import save_data
from conf import setting


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
	def __init__(self, name, age, gender, power, energy, money, confidence, ability):
		super(Player, self).__init__(name, age, gender)
		self.power = power
		self.energy = energy
		self.money = money
		self.confidence = confidence
		self.ability = ability

	# 显示对象属性信息
	def show_info(self):
		print(
			'''
			名  字：{}
			年  龄：{}
			性  别：{}
			体力值：{}
			精力值：{}
			金  钱：{}
			信心值：{}
			能力值：{}

			'''.format(self.name, self.age, self.gender, self.power, self.energy, self.money, self.confidence, self.ability))

	# 存档
	def save_game(self):
		print("正在存档...")
		# 生成一个以当前时间为文件名的存档文件
		file_name = time.strftime('%Y%m%d_%H%M%S', time.gmtime(time.time()))
		db_path = db_handler.handler(setting.DATABASE, file_name)
		save_data.db_write(db_path, self)
		print("存档完成...此次存档文件名为：{}".format(file_name))

	# 睡觉
	def to_sleep(self):
		"""
		睡觉消耗时间，恢复精力
		:return:
		"""
		print("{} 睡觉了。".format(self.name))
		time.sleep(8)
		self.set_attr("energy", 100)

	# 吃饭
	def to_eat(self):
		"""
		吃饭：花费金钱，增加力量值
		:return:
		"""
		menu_dic = setting.GOODS_TYPE["eat"]
		option_dic = OrderedDict()
		for k, v in enumerate(menu_dic, 1):
			option_dic[str(k)] = v
		print("食品目录：")
		for key in option_dic:
			print("{}: {:<15} 价格：{:<10.2f} 元".format(key, option_dic[key], menu_dic[option_dic[key]]["price"]))
			# print("%s:%-10s 价格:%.2f元" % (key, option_dic[key], menu_dic[option_dic[key]]["price"]))
		while True:
			option = input("==>").strip()
			if option in option_dic:
				food_name = option_dic[option]
				money_amount = menu_dic[option_dic[option]]["price"]
				power_amount = menu_dic[option_dic[option]]["power_amount"]
				money_value = self.money - money_amount
				if money_value >= 0:
					power_value = self.power + power_amount
					self.set_attr("money", money_value)
					self.set_attr("power", power_value)
					print("{} 花了 {} 吃了 {}，体力值变为 {}。".format(self.name, money_amount, food_name, self.power))
					break
				else:
					print("钱不够，赶紧去赚钱吧。。。")
					break

	def learn(self):
		"""
		学习：花费金钱，消耗精力，增加能力值
		:return:
		"""
		menu_dic = setting.GOODS_TYPE["learn"]
		option_dic = OrderedDict()
		for k, v in enumerate(menu_dic, 1):
			option_dic[str(k)] = v
		print("学习科目：")
		for key in option_dic:
			print("{}: {:<10} 学费：{:<10.2f} 元。".format(key, option_dic[key], menu_dic[option_dic[key]]["price"]))
		while True:
			option = input("==>").strip()
			if option in option_dic:
				course_name = option_dic[option]
				money_amount = menu_dic[option_dic[option]]["price"]
				energy_amount = menu_dic[option_dic[option]]["energy_amount"]
				ability_amount = menu_dic[option_dic[option]]["ability_amount"]
				money_value = self.money - money_amount
				if money_value >= 0:
					ability_value = self.ability + ability_amount
					energy_value = self.energy - energy_amount
					self.set_attr("money", money_value)
					self.set_attr("ability", ability_value)
					self.set_attr("energy", energy_value)
					print("{} 花了 {} 学了 {}，能力值变为 {}。".format(self.name, money_amount, course_name, self.ability))
					break
				else:
					print("钱不够，赶紧去赚钱吧。。。")
					break

	# 工作
	def work(self):
		"""
		工作：耗费体力值，消耗精力，取得报酬
		:return:
		"""
		menu_dic = setting.GOODS_TYPE["work"]
		option_dic = OrderedDict()
		for k, v in enumerate(menu_dic, 1):
			option_dic[str(k)] = v
		print("工作种类：")
		for key in option_dic:
			print("{}: {:<15} 月薪：{:<10.2f} 元".format(key, option_dic[key], menu_dic[option_dic[key]]["pay"]))
		while True:
			option = input("==>").strip()
			if option in option_dic:
				work_name = option_dic[option]
				pay_amount = menu_dic[option_dic[option]]["pay"]
				print("{} 最终找到了一份 {} 的工作， 月薪：{} 元。".format(self.name, work_name, pay_amount))
				power_amount = menu_dic[option_dic[option]]["power_amount"]
				energy_amount = menu_dic[option_dic[option]]["energy_amount"]
				power_value = self.power - power_amount
				energy_value = self.energy - energy_amount
				# 体力值大于0，精力值大于10，才能上班赚钱
				if power_value >= 0 and energy_value >= 10:
					money_value = self.money + pay_amount
					self.set_attr("money", money_value)
					self.set_attr("power", power_value)
					self.set_attr("energy", energy_value)
					print("{} 花了 {}体力 上了一个月班，赚了 {} 元，体力值变为 {}。".format(self.name, power_amount, pay_amount, self.power))
					break
				else:
					print("快去吃点东西或者睡一觉吧，别累坏了。")
					break

	# 消费
	def consume(self):
		"""
		消费：花费金钱，增加信心值
		:return:
		"""
		menu_dic = setting.GOODS_TYPE["consume"]
		option_dic = OrderedDict()
		for k, v in enumerate(menu_dic, 1):
			option_dic[str(k)] = v
		print("商品名目：")
		for key in option_dic:
			print("{}: {:<15} 价格：{:<15,.2f} 元".format(key, option_dic[key], menu_dic[option_dic[key]]["price"]))
		while True:
			option = input("==>").strip()
			if option in option_dic:
				goods_name = option_dic[option]
				money_amount = menu_dic[option_dic[option]]["price"]
				confidence_amount = menu_dic[option_dic[option]]["confidence_amount"]
				money_value = self.money - money_amount
				if money_value >= 0:
					confidence_value = self.confidence + confidence_amount
					self.set_attr("money", money_value)
					self.set_attr("confidence", confidence_value)
					print("{} 花了 {} 买了 {}，信心值变为 {}。".format(self.name, money_amount, goods_name, self.confidence))
					break
				else:
					print("钱不够，赶紧去赚钱吧。。。")
					break

