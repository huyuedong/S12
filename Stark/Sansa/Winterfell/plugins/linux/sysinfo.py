#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
Linux system info collection script
"""

import os, sys, subprocess
import re


def collect():
	filter_keys = ["Manufacturer", "Serial Number", "Product Name", "UUID", "Wake-up Type"]
	raw_data = {}
	try:
		cmd_result = subprocess.check_output("sudo dmidecode -t system", shell=True)  # 得到系统相关信息
		cmd_result = str(cmd_result)  # 将查询系统命令的结果转换成str
		for key in filter_keys:
			re_compile = re.compile(r'{}:(.+?)\\n'.format(key))  # 动态生成正则条件
			val = re_compile.search(cmd_result)  # 从结果中查找指定的内容
			if val:  # 如果匹配到结果
				raw_data[key] = val.group(1)  # 从匹配结果中的值赋给raw_data[key]
			else:
				raw_data[key] = -1  # 没有结果就把值设为-1
	except Exception as e:
		print("error:", str(e))
		raw_data = dict.fromkeys(filter_keys, -2)

	data = {"asset_type": "server"}
	data["manufacory"] = raw_data["Manufacturer"]

