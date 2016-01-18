#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
深浅copy的区别
"""

import copy
# 数字、字符串:赋值、浅拷贝和深拷贝无差别，因为其永远指向同一个内存地址。
print("字符串的赋值".center(30, '*'))
n1 = 123123
n2 = n1
print(id(n1))
print(id(n2))

print("字符串的赋值".center(30, '*'))
n11 = '123123'
n22 = n11
print(id(n11))
print(id(n22))

print("数字和字符串的浅copy".center(50, '*'))
n3 = copy.copy(n1)
print(id(n1))
print(id(n3))

print("数字和字符串的深copy".center(50, '*'))
n4 = copy.deepcopy(n1)
print(id(n1))
print(id(n4))

# 其他:除了数字和字符串以外，（多层）列表、字典、元祖等在进行赋值、浅copy、深copy时，内存地址是有区别的。
print("其他类的赋值".center(50, '*'))
m1 = {'k1': 123, 'k2': '123', 'k3': [1, 3, 5]}
m2 = m1
print(id(m1))
print(id(m2))

print("其他类的浅拷贝".center(50, '*'))
print("浅copy".center(50, '*'))
m3 = copy.copy(m1)
print("id(m1):%s" % id(m1))
print("id(m3):%s" % id(m3))
# 浅拷贝的m3['k3']这一层指向了同一个内存地址
print("id(m1['k3']):%s" % id(m1['k3']))
print("id(m3['k3']):%s" % id(m3['k3']))

print("其他类的深拷贝".center(30, '*'))
print("深copy".center(30, '*'))
m4 = copy.deepcopy(m1)
print("id(m1):%s" % id(m1))
print("id(m4):%s" % id(m4))
# 深拷贝的m4['k3']这一层指向了不同的内存地址
# 深拷贝就是将除了数字和字符串以外的都重新开辟一个内存空间
print("id(m1['k3']):%s" % id(m1['k3']))
print("id(m4['k3']):%s" % id(m4['k3']))


# 应用：例如监控项配置的修改，要用深copy防止被copy的对象也被修改
print('浅copy会改变被拷贝对象的值'.center(50, '*'))
old_dic = {'cpu': [80, ], 'disk': [70], 'memory': [60]}
# 浅copy之后，更改新字典的话，新旧字典一起更改
new_dic = copy.copy(old_dic)
new_dic['cpu'][0] = 50
print("old_dic:%s" % old_dic)
print("new_dic:%s" % new_dic)

print('深copy不会改变被拷贝对象的值'.center(50, '*'))
old_dic2 = {'cpu': [80, ], 'disk': [70], 'memory': [60]}
# 深copy之后，更改新字典的话，新字典的值改变而旧字典的值不会变
new_dic2 = copy.deepcopy(old_dic2)
new_dic2['cpu'][0] = 50
print("old_dic2:%s" % old_dic2)
print("new_dic2:%s" % new_dic2)
