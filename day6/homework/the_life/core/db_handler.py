#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
处理数据库接口
"""


def file_handler(conn_params, file_name):
	"""
	使用文件存储时返回文件名
	:param file_name: 文件名
	:param conn_params: 数据库参数
	:return: 以存档时间为名的文件
	"""
	db_path = "{}\{}".format(conn_params["path"], file_name)
	return db_path


def handler(conn_params, file_name):
	if conn_params["engine"] == "file_storage":
		return file_handler(conn_params, file_name)
	else:
		pass
