#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
加载或保存用户数据
"""
import pickle
from core import db_handler
from conf import setting


# 操作数据文件
class AccountsDb(object):
	def __init__(self, db_path):
		self.db_path = db_path

	def db_read(self):
		with open(self.db_path, "rb") as fp:
			info = pickle.load(fp)
			return info

	def db_write(self, db_info):
		with open(self.db_path, "rb") as fp:
			pickle.dump(db_info, fp)
		return True
