#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import shelve

p = shelve.open("trade_db")
for i in p.keys():
	print(i, p[i])
print("{}:{}".format(p["000001"]["name"], p["000001"]["price"]))
print(p)
p.close()

