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


# 运算
def calc_func(arg):
	if "*" in arg:
		l_demo = arg.split("*")
		return float(l_demo[0]) * float(l_demo[1])
	elif "/" in arg:
		l_demo = arg.split("/")
		return float(l_demo[0]) / float(l_demo[1])
	elif "+" in arg:
		l_demo = arg.split("+")
		return float(l_demo[0]) + float(l_demo[1])
	elif "-" in arg:
		l_demo = arg.split("-")
		return float(l_demo[0]) - float(l_demo[1])


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

s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# 先去除掉空格
s = re.sub(r'\s+', '', s)
print(s)

# 找到最里面的括号
result = re.search(r'\([^\(\)]+\)', s)
if result:
	# result = result.group()
	print(result.group())
	result = result.group()

# 计算剥离出来的括号里面的值
result2 = calc_func(result.strip("()"))
print(result2)

# 将计算后的值转换成字符串
result2 = str(result2)
print(result2)

# 将源字符串按匹配到的字符串分割成列表
result_list = s.split(result)
print(result_list)

# 将计算后的数值按原位置拼接回去
result5 = result2.join(result_list)
print(result5)
print(type(result5))


result_2 = find_brackets(result5)
if result_2:
	print(result_2)
else:
	print("ERROR!")
