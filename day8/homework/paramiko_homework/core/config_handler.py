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
	with open(setting.CONF, "r") as f:
		config = json.load(f)
	return config


# 写配置文件
def write(configure):
	if type(configure) == dict:
		with open(setting.CONF, "w") as f:
			json.dump(configure, f)
	else:
		loger.error("afferent a invalid configure.")
		raise TypeError


