#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
记录器
"""

import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting


# 记录ATM机操作记录
def my_logger(name, message, level=logging.INFO):
	"""
	ATM操作记录全掌握
	:param name: 记录用户名
	:param message: 信息体
	:param level:日志级别，默认为INFO
	"""
	file_name = setting.LOG_ATM
	logging.basicConfig(filename=file_name, level=level, format="%(asctime)s %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	logging.info("{} {}".format(name, message))

# my_logger("88888881", "log in.")
