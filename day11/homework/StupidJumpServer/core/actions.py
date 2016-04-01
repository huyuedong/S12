#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
命令行参数解析，功能引导
"""

import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import action_registers

logger = logging.getLogger(__name__)


# 帮助信息
def help_msg():
	print("Here are the available commands:")
	for key in action_registers.actions:
		print(key)


# 定义从命令行启动
def start_by_command(argvs):
	if len(argvs) < 2:
		help_msg()
	elif argvs[1] == "?" or argvs[1] == "/?":
		help_msg()
	elif argvs[1] not in action_registers.actions:
		raise SystemExit("Invalid command:{}".format(argvs[1]))
	else:
		action_registers.actions[argvs[1]](argvs[1:])
