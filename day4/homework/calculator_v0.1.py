#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
计算器开发
-1.实现加减乘除及括号优先级解析
-2.用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
-  必须自己解析里面的(),+,-,*,/符号和公式，运算后得出结果，结果必须与真实的计算器所得出的结果一致
"""
import re


# 乘除运算
def mul_div_func(arg):
	if "*" in arg:
		l_demo = arg.split("*")
		lift_num = check_sign(l_demo[0])
		right_num = check_sign(l_demo[1])
		return lift_num * right_num
	elif "/" in arg:
		l_demo = arg.split("/")
		lift_num = check_sign(l_demo[0])
		right_num = check_sign(l_demo[1])
		return lift_num / right_num
	else:
		return arg


# 加减运算
def add_sub_func(arg):
	if "+" in arg:
		l_demo = arg.split("+")
		lift_num = check_sign(l_demo[0])
		right_num = check_sign(l_demo[1])
		return lift_num + right_num
	elif "-" in arg:
		l_demo = arg.split("-")
		lift_num = check_sign(l_demo[0])
		right_num = check_sign(l_demo[1])
		return lift_num + right_num
	else:
		return arg


# 找括号
def find_brackets(arg):
	tmp = re.search(r'\([^\(\)]+\)', arg)
	if tmp:
		return tmp.group()
	else:
		return None


# 判断正负号
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


# 分离操作数
def split_num(str_demo, operator):
	list_tmp = str_demo.split(operator)
	lift_num = check_sign(list_tmp[0])
	right_num = check_sign(list_tmp[1])
	return [lift_num, right_num]


# 数值转字符串
def int_to_str(arg):
	if float(arg) >= 0:
		arg = str(arg)

		return "+{}".format(arg)
	else:
		arg = str(arg)
		return arg


# 找乘或除
def find_mul_div(arg):
	tmp = re.search(r'[\+\-]?\d*\.?\d+[\*\/][\+\-]?\d*\.?\d+', arg.strip("()"))
	if tmp:
		return tmp.group()
	else:
		return None


# 找加或减
def find_add_sub(arg):
	tmp = re.search(r'[\+\-]?\d*\.?\d+[\+\-][\+\-]]?\d*\.?\d+', arg.strip("()"))
	if tmp:
		return tmp.group()
	else:
		return None


s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
s = "1+2*3/(4*5)"
# 先去除掉空格
s = re.sub(r'\s+', '', s)
print(s)
loop_flag = True
while loop_flag:
	# 在s中找括号
	bracket_str = find_brackets(s)
	init_bracket_str = bracket_str
	print(bracket_str)
	# 有括号
	if bracket_str:
		while True:
			# 在括号里找乘、除
			str_tmp = find_mul_div(bracket_str)
			print(str_tmp)
			if str_tmp:
				str_1 = mul_div_func(str_tmp)
				str_1 = int_to_str(str_1)
				print(str_1)
				bracket_str = str_1.join(bracket_str.split(str_tmp))
				print(bracket_str)
			# 找不到乘除了
			else:
				# 在括号里找加、减
				print(bracket_str)
				str_tmp2 = find_add_sub(bracket_str)
				if str_tmp2:
					str_1 = add_sub_func(str_tmp2)
					str_1 = int_to_str(str_1)
					bracket_str = str_1.join(bracket_str.strip("()").split(str_tmp2))
				else:
					s = bracket_str.join(s.split(bracket_str))
					break
			s = str_1.join(s.split(bracket_str))
	# 没有括号
	else:
		str_tmp = find_multi_div(s)
		if str_tmp:
			str_1 = calc_func(str_tmp)
			str_1 = int_to_str(str_1)
			print(str_1)
			s = str_1.join(s.strip("()").split(str_tmp))
			print(s)
		else:
			# 找加、减
			str_tmp = find_add_sub(s)
			if str_tmp:
				str_1 = calc_func(str_tmp)
				str_1 = int_to_str(str_1)
				bracket_str = str_1.join(s.strip("()").split(str_tmp))
			else:
				print(s)
				break
