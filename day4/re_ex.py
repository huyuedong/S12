#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
正则表达式的练习
"""

import re
# s1 = "a b   c"
# print(s1.split(' '))
# print(re.split(r'\s+', s1))    # \s+:一个或多个空格
#
# p = re.compile(r'^[0-9]')   # 生成正则对象,提前解析匹配规则
# m = p.match("1234Abc")  # match匹配到时返回一个Match对象，否则返回None
# n = p.match("Abc1234")
# print(m)
# print(n)
# t = re.match(r'[0-9]+', "234abc234")
# print(t)
#
# # 从字符串中查找手机号码
# info = "hey my name is alex, and my phone number is 18651054604, please call me if you are pretty!"
# result = re.search(r'(1)[3578]\d{9}', info)
# if result:
# 	print(result.group())
# # 匹配输入的是否为正确的手机号格式
# phone_num = input("Please input your phone number:")
# result2 = re.match(r'^1[3578]\d{8}[0-9]$', phone_num)
# if result2:
# 	print("Your phone number is {}.".format(result2.group()))
# else:
# 	print("Invalid number.")


# 字符串中查找IP
# ip_addr = "inet 192.168.60.223 netmask 0xffffff00 broadcast 192.168.60.255"
# p = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# result = p.search(ip_addr)
# if result:
# 	print(result.group())
#
# # 判断输入是否为合法IP
# ip_info = input("Please input the IP:").strip()
# result2 = re.search(r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$', ip_info)
# if result2:
# 	print("Your IP is: {}".format(result2.group()))
# else:
# 	print("Invalid input")


# 分组匹配?
contactInfo = "Oldboy School, Beijing Changping Shahe: 010-8343245"
match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
if match:
	print(match.groups())
else:
	print("eeeeeee")

# 匹配email


