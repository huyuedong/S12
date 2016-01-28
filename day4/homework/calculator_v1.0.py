#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
计算器开发
-1.实现加减乘除及括号优先级解析
-2.用户输入 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )等类似公式后，
-  必须自己解析里面的(),+,-,*,/符号和公式，运算后得出结果，结果必须与真实的计算器所得出的结果一致
Version:1.0
Create:2016.01.28
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
		if len(l_demo) == 2:
			lift_num = check_sign(l_demo[0])
			right_num = check_sign(l_demo[1])
			return lift_num - right_num
		elif len(l_demo) == 3:
			lift_num = check_sign(l_demo[1])
			right_num = check_sign(l_demo[2])
			return 0 - lift_num - right_num
	else:
		pass


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
		else:
			result_tmp = float(arg)
			return result_tmp


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
	tmp = re.search(r'[\+\-]?\d*\.?\d+[\*\/][\+\-]?\d+\.?\d*', arg.strip("()"))
	if tmp:
		return tmp.group()
	else:
		return None


# 找加或减
def find_add_sub(arg):
	tmp = re.search(r'[\+\-]?\d*\.?\d+[\+\-]\d+\.?\d*', arg.strip("()").lstrip("+"))
	if tmp:
		return tmp.group()
	else:
		return None


# 优化算式
def optimize_formula(arg):
	arg = re.sub(r'\-{2}', "+", arg)
	arg = re.sub(r'\+{2}', "+", arg)
	arg = re.sub(r'\+\-', "-", arg)
	arg = re.sub(r'\-\+', "-", arg)
	return arg


# 获取输入并判断输入的算式是否合法
def get_input():
	while True:
		print("SimpleCalculator".center(50, '*'))
		s = input("Please input the equation,(enter 'Q' to quit):").strip()
		if s.upper() == 'Q':
			return 'Q'
		else:
			result_list = []
			result_list.append(re.search(r'\([\*\/%]+\d', s))
			result_list.append(re.search(r'^[\*\/%]+\d', s))
			result_list.append(re.search(r'\d[\.\*\/%]+$', s))
			result_list.append(re.search(r'\d[\*\/%]+\)', s))
			result_list.append(re.search(r'[\(\)\d%]+\(', s))
			result_list.append(re.search(r'[\*\\]{3,}', s))
			result_list.append(re.search(r'[%%]{2,}', s))
			result_list.append(re.search(r'[^0-9\.\+\-\*\/\(\)\s]', s))
			result_list.append(s.count("(") != s.count(")"))
			result_list.append(len(s) == 0)
			if any(result_list):
				print("Invalid input,please try again!")
			else:
				return s


# 运算
def operating(arg):
	while True:
		# 从左往右找乘、除
		str_tmp = find_mul_div(arg)
		# 找到乘、除
		if str_tmp:
			str_1 = mul_div_func(str_tmp)
			str_1 = int_to_str(str_1)
			arg = arg.replace(str_tmp, str_1)
		# 找不到乘、除
		else:
			# 找加、减
			arg = optimize_formula(arg)
			str_tmp = find_add_sub(arg.lstrip("+"))
			# 找到加、减
			if str_tmp:
				str_1 = add_sub_func(str_tmp)
				str_1 = int_to_str(str_1)
				arg = arg.replace(str_tmp, str_1)
			# 找不到加、减
			else:
				return arg.strip("()").lstrip("+")


# 主函数
def main():
	while True:
		s = get_input()
		if s == 'Q':
			break
		else:
			# 去掉字符串空格
			s = re.sub(r'\s+', "", s)
			# 保存原始输入
			original_s = s
			while True:
				# 找括号
				bracket_str = find_brackets(s)
				# 有括号
				if bracket_str:
					# 保存原始括号内容
					original_bracket_str = bracket_str
					# 计算括号内的值
					bracket_str = operating(bracket_str)
					# 用计算出的值去替换源字符串中的括号
					s = s.replace(original_bracket_str, bracket_str)
				# 无括号
				else:
					# 从左往右计算值
					result = operating(s)
					# 结果为\d+.0时，去掉.0
					if result.endswith(".0"):
						result = result.rstrip(".0")
					print("{}={}".format(original_s, result))
					break


if __name__ == '__main__':
	main()
