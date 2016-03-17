#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
try to parse instruction
"""

import re

demo1 = "mysalt -g 'group1, group2' file.get 'httpd.conf'"


l1 = demo1.split()

print(l1)
for i in l1:
	print(i)


l3 = list(map(lambda t: re.sub(r'[,"\']', "", t), l1))
print(l3)


