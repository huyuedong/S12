#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
加载或保存用户数据
"""
import pickle


# 读存档文件
def db_read(db_path):
	with open(db_path, "rb") as fp:
		info = pickle.load(fp)
		return info


# 写存档文件
def db_write(db_path, db_info):
	with open(db_path, "ab") as fp:
		pickle.dump(db_info, fp)
	return True
