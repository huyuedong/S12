#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
记录器
"""

import logging
import os


# 记录ATM机操作记录
def my_logger(name, str, level=logging.INFO):
	"""
	ATM操作记录全掌握
	:param name: 记录用户名
	:param str: 信息体
	:param level:日志级别，默认为INFO
	"""
	base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	atm_log_file = os.path.join(base_path, "database\log.atm")
	file_name = atm_log_file
	logging.basicConfig(filename=file_name, level=level, format="%(asctime)s %(message)s", datefmt="%y-%m-%d %H:%M:%S")
	logging.info("{} {}".format(name, str))

