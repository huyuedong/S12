#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
序列化：pickle和json模块
"""
import pickle
import json

# 四种方法：dump、dumps、load、loads
# info = {"name": "alex", "age": 18, "Limit": 10000, "created": "2016-02-01"}

# with open("test.txt", "wb") as f:
# 	f.write(pickle.dumps(info))
#
# with open("test.txt", "rb") as p:
# # 	d1 = pickle.loads(p.read())
# 	d1 = pickle.load(p)
#
# for k in d1:
# 	print(k, d1[k])
#
# if d1.get("Limit", 0) > 5000:
# 	print("haha")

# 四种方法：dump、dumps、load、loads
info = {"name": "alex", "age": 18, "Limit": 10000, "created": "2016-02-01"}
#
with open("test2.txt", "w") as f:
	json.dump(info, f)
	# f.write(json.dumps(info))

with open("test2.txt", "r") as p:
	d2 = json.load(p)

for k in d2:
	print(k, d2[k])
