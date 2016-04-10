#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


num = 3
while num < 10:
	if num == 5:
		num += 1
		continue
	if num == 7:
		break
	print(num)
	num += 1
