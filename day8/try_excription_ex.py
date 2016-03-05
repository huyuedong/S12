#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
异常处理的练习
"""

while True:
	# Ctrl+C 需要在输入阶段就捕获异常
	try:
		name = input("name:")
		age = input("age:")
		name = int(name)
		age = int(age)
		age += 1
		print("name:{},age:{}".format(name, age))
	except ValueError as e:
		print("Value Error:{}".format(e))
	except KeyboardInterrupt as e:
		print("Ctrl + C:{}".format(e))
		print("Going to exit...")
		break
	except Exception:
		print("Unknow Error!")
	# 没有异常时执行else下命令
	else:
		print("NO ERROR!")
	# 无论如何都执行finally下的命令
	finally:
		print("It's the end of try...")
