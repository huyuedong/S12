#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
测试db
"""

import pickle
import shelve

with open("trade_db.dat.dat", "rb") as f:
	d1 = pickle.load(f)
	# for k in d1.keys():
	# 	print(k)
	# for i in d1:
	# 	print(i)
	print(d1)

# d2 = shelve.open("trade_db.dat.dat")
# print(d2)
# d2.close()
