#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
数据库读写
"""

import pickle


# 读取用户数据库
def read_db(arg):
	with open(arg, "rb") as fp:
		return pickle.load(fp)


# 写入用户数据库
def write_db(file=None, data=None):
	with open(file, "wb") as fp:
		fp.write(pickle.dumps(data))
