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
		n = 0
		flag = False
		for line in f:
			if line.strip().startswith('backend'):
				n += 1
				dic_tmp[n] = []
				dic_tmp[n].append(line.split()[1])
				flag = True
			elif all([flag, line.strip().startswith("server")]):
				dic_tmp[n].append(line.strip())
				continue
	backend_dic = OrderedDict()
	for i in dic_tmp.items():
		tmp = i[1][0]
		i[1].pop(0)
		backend_dic[tmp] = i[1]
	# return backend_dic

	# dic = init_backend_info()
	print("当前backend配置信息如下：")
	for k in backend_dic.keys():
		print("backend {}".format(k))
		for v in backend_dic.get(k):
			print("{}{}".format(" " * 8, v))
		print("\n")
