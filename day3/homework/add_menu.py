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
list1 = ["server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000", "server 100.1.7.10 100.1.7.10 weight 20 maxconn 3000", "server 100.1.7.11 100.1.7.11 weight 20 maxconn 3000"]

flag = True
with open('write_test1.txt', 'r+') as f1, open('write_test2.txt', 'w+') as f2:
	for line in f1:
		if line.strip() == "backend www.oldboy.org":
			f2.write(line)
			flag = False
			for i in list1:
				f2.write("{}{}\n".format(' ' * 8, i))
		elif line.startswith("backend"):
			f2.write(line)
			flag = True
		elif all([flag, line]):
			f2.write(line)



