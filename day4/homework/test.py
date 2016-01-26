#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import re

s = "1+3*(-60/2)+4"
result = re.search(r'\(.+\)', s)
if result:
	print(result.group())
	m = result.group().strip("()")

	if "/" in m:
		l = m.split("/")
		print(int(l[0]) / int(l[1]))
		print(float(l[0]) / float(l[1]))
