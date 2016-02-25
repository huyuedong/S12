#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
测试读取存档
"""

import os
import re

file_path = os.path.dirname(__file__)
l1 = os.listdir(file_path)
save_list = []
for i in l1:
	if re.match(r'^\d{8}_\d{6}$', i):
		save_list.append(i)
for k, v in enumerate(save_list, 1):
	print("{}:{}".format(k, v))

