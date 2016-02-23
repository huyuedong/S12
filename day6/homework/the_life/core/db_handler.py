#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
处理数据库接口
"""


class DbHandler(object):
	def __init__(self, conn_params):
		self.conn_params = conn_params

	def file_handler(self, conn_params):
		"""
		使用文件存储时返回文件名
		:param conn_params: 数据库参数
		:return:
		"""
		db_path = "{}\{}".format(self.conn_params["path"], self.conn_params["name"])
		return db_path

	def handler(self, conn_params):
		if conn_params["engine"] == "file_storage":
			return DbHandler.file_handler(self, conn_params)
		else:
			pass
