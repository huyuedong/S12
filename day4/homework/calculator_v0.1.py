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
	tmp = re.search((r'\([^\(\)]+\)]', arg))
	if tmp:
		return tmp.group()
	else:
		return None

s = "1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# 先去除掉空格
s = re.sub(r'\s+', '', s)
print(s)

# 找到最里面的括号
result = re.search(r'\([^\(\)]+\)', s)
if result:
	print(result.group())

# 将匹配到的结果去除括号
result = result.group().strip("()")

result2 = calc_func(result)
print(result2)
result2 = str(result2)

# 将字符串的前面和后面放进列表，把匹配到的字符串算出数值之后再传进去
result3 = s.split(result)
result5 = result2.join(result3)
print(result5)
print("{0}{1}{2}".format(result3[0], result2, result3[1]))

# result = find_brackets(result3)
# if result:
# 	result = result.strip("()")
# 	result4 = calc_func(result)
# 	print(result4)
# else:
# 	print("ERROR!")
