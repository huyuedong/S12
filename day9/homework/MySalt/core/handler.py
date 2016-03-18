#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
yaml handler
"""

import yaml
import sys
import os
import re
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting
loger = logging.getLogger(__name__)


def myhandler(arg):
	ip_list = list()
	loger.debug("get the arg:{}".format(arg))
	with open(setting.GROUPS_INFO) as f:
		info = yaml.load(f)
	try:
		# 如果传过来的参数时*就把所有的IP记录都返回
		if len(arg) == 1 and arg[0] == "*":
			for i in info["groups"]:
				ip_list.extend(info["groups"][i])
				ip_list = list(set(ip_list))
		# 如果以-g开头的话，就返回指定组名的IP
		elif arg[0] == "-g":
			loger.debug("begin to get group name: {}".format(arg))
			arg = arg[1:]
			loger.debug("get the group list: {}".format(arg))
			for i in arg:
				if info["groups"].get(i):
					ip_list.extend(info["groups"][i])
					ip_list = list(set(ip_list))
		# 如果以-h开头的话，就返回指定IP
		elif arg[0] == "-h":
			arg = arg[1:]
			for i in arg:
				if re.match(r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$', i):
					ip_list.append(i)
		else:
			pass
	except IndexError as e:
		loger.debug("myhandler get invalid arguments:{}, error:{}.".format(arg, e))
	finally:
		return ip_list

