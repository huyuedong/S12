#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import re


def check_sign(arg):
	if arg.startswith("-"):
		result_tmp = 0 - float(arg.strip("-"))
		return result_tmp
	elif arg.startswith("+"):
		result_tmp = float(arg.strip("+"))
		return result_tmp
	else:
		result_tmp = float(arg.strip())
		return result_tmp

s = "1-2*((60-30+-8.0*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))"
s = "-3-9"
init_s = s
loop_flag = True
while loop_flag:
	result = re.search(r'\([^\(\)]+\)', s)
	if result:
		print(result.group())

		finded_result = result.group()
		init_find_result = finded_result
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
				finded_result = re.sub(r'\-{2}', "+", finded_result)
				finded_result = re.sub(r'\+{2}', "+", finded_result)
				finded_result = re.sub(r'(\-\+)', "-", finded_result)
				finded_result = re.sub(r'(\+\-)', "-", finded_result)
				print(finded_result)
				n2 = re.search(r'[\+\-]?\d*\.?\d+[\+\-]\d+\.?\d*', finded_result)
				if n2:
					print(n2.group())
					finded_n = n2.group().lstrip("+")
					if "+" in finded_n:
						n_list = finded_n.split("+")
						print(n_list)
						lift_num = check_sign(n_list[0])
						right_num = check_sign(n_list[1])
						print(lift_num + right_num)
						a = lift_num + right_num
						a = str(a)
						if float(a) >= 0:
							a = "+{}".format(a)
						b = a.join(finded_result.strip("()").split(finded_n))
						print(b)
						finded_result = b
					elif "-" in finded_n:
						n_list = finded_n.split("-")
						print(n_list)
						if len(n_list) == 2:
							lift_num = check_sign(n_list[0])
							right_num = check_sign(n_list[1])
							print(lift_num - right_num)
							a = lift_num - right_num
							a = str(a)
						elif len(n_list) == 3:
							lift_num = check_sign(n_list[1])
							right_num = check_sign(n_list[2])
							print(0 - lift_num - right_num)
							a = 0 - lift_num - right_num
							a = str(a)
						if float(a) >= 0:
							a = "+{}".format(a)
						b = a.join(finded_result.strip("()").split(finded_n))
						print(b)
						finded_result = b
				else:
					print(finded_result.lstrip("+"))
					s = finded_result.lstrip("+").join(s.split(init_find_result))
					break
	else:
		print(s)
		while True:
			n = re.search(r'[\+\-]?\d*\.?\d+[\*\/][\+\-]?\d*\.?\d+', s)
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
					b = a.join(s.split(finded_n))
					print(b)
					s = b
				elif "/" in finded_n:
					n_list = finded_n.split("/")
					lift_num = check_sign(n_list[0])
					right_num = check_sign(n_list[1])
					print(lift_num / right_num)
					a = lift_num / right_num
					a = str(a)
					if float(a) >= 0:
						a = "+{}".format(a)
					b = a.join(s.split(finded_n))
					print(b)
					s = b
				else:
					print("Error!")
			else:
				print(s)
				s = re.sub(r'\-{2}', "+", s)
				s = re.sub(r'\+{2}', "+", s)
				s = re.sub(r'(\-\+)', "-", s)
				s = re.sub(r'(\+\-)', "-", s)
				print(s)
				n2 = re.search(r'[\+\-]?\d*\.?\d+[\+\-]\d+\.?\d*', s)
				if n2:
					print(n2.group())
					finded_n = n2.group().lstrip("+")
					if "+" in finded_n:
						n_list = finded_n.split("+")
						print(n_list)
						lift_num = check_sign(n_list[0])
						right_num = check_sign(n_list[1])
						print(lift_num + right_num)
						a = lift_num + right_num
						a = str(a)
						if float(a) >= 0:
							a = "+{}".format(a)
						b = a.join(s.split(finded_n))
						print(b)
						s = b
					elif "-" in finded_n:
						n_list = finded_n.split("-")
						print(n_list)
						if len(n_list) == 2:
							lift_num = check_sign(n_list[0])
							right_num = check_sign(n_list[1])
							print(lift_num - right_num)
							a = lift_num - right_num
							a = str(a)
						elif len(n_list) == 3:
							lift_num = check_sign(n_list[1])
							right_num = check_sign(n_list[2])
							print(0 - lift_num - right_num)
							a = 0 - lift_num - right_num
							a = str(a)
						a = str(a)
						if float(a) >= 0:
							a = "+{}".format(a)
						b = a.join(s.split(finded_n))
						print(b)
						s = b
				else:
					print("{}的计算结果是：{}".format(init_s, s.lstrip("+")))
					loop_flag = False
					break
