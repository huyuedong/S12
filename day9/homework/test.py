#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
测试模块导入
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import importlib


user_input = input("==>").strip()

# try:
# 	module_func_list = user_input.split(".")
# 	module_name = module_func_list[0]
# 	func_name = module_func_list[1]
# 	module = importlib.import_module("mysalt.{}".format(module_name))
# 	print(module)
# 	if hasattr(module, func_name):
# 		print("OK!")
# except [ValueError, IndexError, TypeError] as e:
# 	print("Error!", e)


l1 = user_input.split()[1:]
if l1[0] == "*":
	print("OK!")

# for i in l1:
# 	print(i)
