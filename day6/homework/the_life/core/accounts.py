#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
加载或保存用户数据
"""
import pickle
from core import db_handler
from conf import setting


class Accounts(object):
	def __init__(self, db_path):
		self.db_path = db_path

	def db_read(self):
		pass

	def db_write(self):
		pass
