#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
try to parse instruction
"""

import re

demo1 = "mysalt '*' cmd.run 'df -h'"
demo2 = "mysalt -g 'group1, group2' cmd.run 'df -h'"


l1 = demo1.split()
l2 = demo2.split()

print(l1)
for i in l1:
	print(i)
cmd_list = list()
op_obj_list = list()
op_obj_tmp = l2[l2.index("-g")+1:l2.index("cmd.run")]
print(op_obj_tmp)
# for i in op_obj_tmp:
# 	print("==>", i)
# 	print("<==", re.sub(r'[,"\']', "", i))
# 	op_obj_list.append(re.sub(r'[,"\']', "", i))
# print(op_obj_list)
# for i in op_obj_list:
# 	print(i)
# op_obj = " ".join(op_obj_tmp)
# print(op_obj)
# print("*" * 50)
# re.sub(r'[,"\']', "", op_obj)
# print(op_obj)
# print("=" * 50)
# print(l2)
# for i in l2:
# 	print(i)

l3 = list(map(lambda t: re.sub(r'[,"\']', "", t), l1))
l4 = list(map(lambda t: re.sub(r'[,"\']', "", t), l2))
print(l3)
print(l4)

flag = False
for i in l4:
	if i.count(".") > 0:
		flag = True
		print(l4.index(i))
if flag:
	print("OK!")
