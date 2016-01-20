#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
实现在配置文件下对应的url下添加server信息的功能
	-输入：
		arg = {
			'backend': 'www.oldboy.org',
			'record':{
				'server': '100.1.7.9',
				'weight': 20,
				'maxconn': 30
			}
		}
	-添加到对应的backend下
"""
from functools import reduce
list1 = ["server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000", "server 100.1.7.10 100.1.7.10 weight 20 maxconn 3000", "server 100.1.7.11 100.1.7.11 weight 20 maxconn 3000"]

# flag = True
# with open('write_test1.txt', 'r+') as f1, open('write_test2.txt', 'w+') as f2:
# 	for line in f1:
# 		if line.strip() == "backend www.oldboy.org":
# 			f2.write(line)
# 			flag = False
# 			for i in list1:
# 				f2.write("{}{}\n".format(' ' * 8, i))
# 		elif line.startswith("backend"):
# 			f2.write(line)
# 			flag = True
# 		elif all([flag, line]):
# 			f2.write(line)


arg = {
			'backend': 'www.oldboy.org',
			'record': {
				'server': '100.1.7.9',
				'weight': 20,
				'maxconn': 30
			}
		}

# 如果用户输入server时输入hostname和IP的话可以使用reduce
d1 = arg.get('record')
l1 = []
for k, v in d1.items():
	l1.append("{} {}".format(k, v))
s1 = reduce(lambda x, y: "{} {}".format(x, y), l1)
print(s1)

# 如果用户输入server时只输入了IP的话使用下面的方法
s2 = "server {} {} weight {} maxconn {}".format(d1.get('server'), d1.get('server'), d1.get('weight'), d1.get('maxconn'))
print(s2)
