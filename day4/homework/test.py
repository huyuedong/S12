#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import re

def check_sign(arg):
	if isinstance(arg, str):
		if arg.startswith("-"):
			result_tmp = 0 - float(arg.strip("-"))
			return result_tmp
		elif arg.startswith("+"):
			result_tmp = float(arg.strip("+"))
			return result_tmp
		elif arg.isdigit():
			result_tmp = float(arg)
			return result_tmp
		else:
			return "Error!"
	else:
		return "ParamTypeError!"

s = "1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
# while True:
result = re.search(r'\([^\(\)]+\)', s)
if result:
	print(result.group())

	finded_result = result.group()
	while True:
		# 从左往右查找*或/
		n = re.search(r'[\+\-]?\d*\.?\d+[\*\/][\+\-]?\d*\.?\d+', finded_result.strip("()"))
		if n:
			print(n.group())
			finded_n = n.group()
			if "*" in finded_n:
				n_list = finded_n.split("*")
				lift_num = check_sign(n_list[0])
				right_num = check_sign(n_list[1])
				print(lift_num * right_num)
				a = lift_num * right_num
				a = str(a)
				if float(a) >= 0:
					a = "+{}".format(a)
				b = a.join(finded_result.strip("()").split(finded_n))
				print(b)
				finded_result = b
			elif "/" in finded_n:
				n_list = finded_n.split("/")
				lift_num = check_sign(n_list[0])
				right_num = check_sign(n_list[1])
				print(lift_num / right_num)
				a = lift_num / right_num
				a = str(a)
				if float(a) >= 0:
					a = "+{}".format(a)
				b = a.join(finded_result.strip("()").split(finded_n))
				print(b)
				finded_result = b
			else:
				print("Error!")
		else:
			print(finded_result)
			break

