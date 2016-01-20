#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
初始化backend信息
"""

from collections import OrderedDict


def init_backend_info():
	dic_tmp = {}
	with open('haproxy.cfg', 'r') as f:
		n = 1
		flag = False
		for line in f:
			if line.strip().startswith('backend'):
				dic_tmp[n] = []
				dic_tmp[n].append(line.split()[1])
				flag = True
				n += 1
			elif all([flag, line.strip().startswith("server")]):
				dic_tmp[n-1].append(line.strip())
				continue
	backend_dic = OrderedDict()
	for i in dic_tmp.items():
		tmp = i[1][0]
		i[1].pop(0)
		backend_dic[tmp] = i[1]
	return backend_dic

dic = init_backend_info()

for k in dic.keys():
	print(k)
	for v in dic.get(k):
		print(v)
	print("=" * 50)
