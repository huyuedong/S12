#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
str类的内建方法练习

"""
name1 = 'alex'
name2 = str('ERIC')    # 调用字符串类的__init__()方法
print(type(name1))
print(dir(name1))    # 打印出类的成员

# 包含
result = name1.__contains__('er')
print(result)
result = 'er' in name1
print(result)

#
result = name2.casefold()
print(result)

# 居中
# print('*' * 8 %s '*' * 8 % name1)
result = name1.center(20, '*')
print(result)

# count
str1 = 'adasafafdsfqadasddfa'
result = str1.count('a')
print(result)

# encode
result = name1.encode('gbk')
print(result)

# endswith
result = str1.endswith('a')
print(result)
result = str1.endswith('s', 2, 4)
print(result)

# 所有首字母大写
str2 = 'alex is sb!'
result = str2.title()
print(result)
