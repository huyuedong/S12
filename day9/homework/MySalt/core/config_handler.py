#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
操作配置文件的模块
"""

import json
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting
loger = logging.getLogger(__name__)


# 读配置文件
def read():
	with open(setting.CONFIG, "r") as f:
		config = json.load(f)
	return config


# 写配置文件
def write(configure):
	if type(configure) == dict:
		pop_list = []
		for k in configure:
			configure[k] = list(set(configure[k]))  # 将主机列表去重
			if not configure[k]:
				pop_list.append(k)
		# 去掉空的组
		for i in pop_list:
			configure.pop(i)
		with open(setting.CONFIG, "w") as f:
			json.dump(configure, f)
	else:
		loger.error("afferent a invalid configure.")
		raise TypeError


