#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
使用Python实现多态
"""


# 定义父类Animal
class Animal:
	def __init__(self, name):    # Constructor of the class
		self.name = name

	# 定义一个供子类复写的方法
	def talk(self):              # Abstract method, defined by convention only
		raise NotImplementedError("Subclass must implement abstract method")


# 定义子类Cat
class Cat(Animal):
	def talk(self):
		return 'Meow!'


# 定义子类Dog
class Dog(Animal):
	def talk(self):
		return 'Woof! Woof!'

# 实例化一个Cat、一个Dog
animals = [Cat('Missy'), Dog('Lassie')]


for animal in animals:
	print("{} : {}".format(animal.name, animal.talk()))
