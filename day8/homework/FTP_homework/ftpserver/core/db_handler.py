#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
处理用户数据库
"""
import json


def file_handler_read(db_params):
	"""
	使用文件存储时返回文件名
	:param db_params: 数据库参数
	:return: 字典类型的数据
	"""
	db_path = "{}/{}".format(db_params["path"], db_params["name"])
	with open(db_path, "r") as f:
		info = json.load(f)
	return info


def file_handler_write(info, db_params):
	db_path = "{}/{}".format(db_params["path"], db_params["name"])
	with open(db_path, "w") as f:
		json.dump(info, f)


# def handler(db_params):
# 	if db_params["engine"] == "file_storage":
# 		return file_handler(db_params)
# 	else:
# 		pass