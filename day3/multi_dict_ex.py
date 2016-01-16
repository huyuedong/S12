#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
白宇
"""

old_dict = {
	"#1": {'hostname': 'c1', 'cpu_count': 2, 'mem_capacity': 80},
	"#2": {'hostname': 'c2', 'cpu_count': 3, 'mem_capacity': 90},
	"#3": {'hostname': 'c3', 'cpu_count': 4, 'mem_capacity': 100},
}
# print(old_dict.values())
#
# l1 = []
# for i in old_dict.values():
# 	for item in i.items():
# 		l1.append(item)
# print(l1)
# print(l1[0])
l1 = []
for i in old_dict.values():
	l1.append(list(i.items()))
# print(l1)

l2 = list(zip(* l1))
print(l2)

for i in range(len(l2)):
	list(l2[i])
print(l2)
# 	print(dict(list((i))))
