#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
dict内建的方法
* 字典是无序的
* from collections import OrderedDict   # 有序字典
"""

dic1 = {'k1': 'v1', 'k2': 'v2', }
print(dic1)
dic1 = dict(k1='v1', k2='v2')
print(dic1)

# 清空
dic1.clear()
print(dic1)

# 复制 copy()分为深拷贝和浅拷贝 此处为浅拷贝(shallow copy)

# fromkeys: Returns a new dict with keys from iterable and values equal to value.
dic2 = dict.fromkeys(['k1', 'k2', ], 1)
print(dic2)

# 取得指定键的值-> get(self, k, d=None)
dic1 = {'k1': 'v1', 'k2': 'v2'}
print(dic1.get('k1'))
print(dic1.get('k3', 'No!!!'))

# 键值对的集合：items()
print(dic1.items())
for i in dic1.items():
	print(i)

# 键值
print(dic1.keys())
for i in dic1.keys():
	print(i)

print('line:39'.center(20, '='))

# 弹出： 移除指定的键，返回对应的值 -> pop(self, k, d=None)
print(dic1.pop('k1'))
print(dic1)
print(dic1.pop('k3', 'ERROR!!!'))

# popitem() 弹出一个键值对组成的元祖，字典为空弹出时报错
dic1 = {'k1': 'v1', 'k2': 'v2'}
print(dic1.popitem())
print(dic1)
print(dic1.popitem())

# 为字典设置默认值
dic1 = {}
dic1.setdefault('k1', 'v1')
dic1.setdefault('k2')
print(dic1)

# 升级字典
dic1 = {'k1': 'v1', }
dic2 = {'k2': 'v2', 'k3': 'v3', }
dic1.update(dic2)
print(dic1)
print(dic2)

# 返回字典的值
dic1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', }
print(dic1.values())
for i in dic1.values():
	print(i)

# 课堂小练习
# [11, 22, 33, 44, 55, 66, 77, 88, 99, ...]大于66的保存在字典的第一个key的值中，小于等于66的放到第二个key的值中
# {'key1':大于66的， 'key2':小于等于66的}

l1 = [11, 22, 33, 44, 55, 66, 77, 88, 90, 99, ]
dic = {}
for i in l1:
	if i > 66:
		if 'key1' in dic.keys():
			dic['key1'].append(i)
		else:
			dic['key1'] = [i, ]
	else:
		if 'key2' in dic.keys():
			dic['key2'].append(i)
		else:
			dic['key2'] = [i, ]
print(dic)
