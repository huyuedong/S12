#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
解析file.sls文件
"""

import yaml
import sys
import os
import re
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting
loger = logging.getLogger(__name__)


def parse_file(key, arg):
	arg_list = []
	with open(setting.FILE_INFO) as f:
		info = yaml.load(f)
		source_path = info[key]["default"]["source"]
		destination_path = info[key]["default"]["name"]
		for i in arg:
			source_file = "{}{}{}".format(source_path, os.sep, i)
			destination_file = "{}{}{}".format(destination_path, os.sep, i)
			# 遍历判断要传送的文件存不存在
			if os.path.isfile("{}{}{}".format(source_path, os.sep, i)):
				arg_list.append([source_file, destination_file])
	return arg_list
