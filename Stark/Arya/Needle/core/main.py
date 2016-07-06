#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
needle 主函数
"""

from conf import configs, registered_modules
import pika
import platform
import subprocess
import json, threading
from modules import files


class CommandManagement(object):
	def __init__(self, argvs):
		self.argvs = argvs[1:]
		self.argv_handler()

	def argv_handler(self):
		if len(self.argvs) == 0:
			exit("argument: start\stop")
		if hasattr(self, self.argvs[0]):
			func = getattr(self, self.argvs[0])
			func()
		else:
			exit("invalid argument.")

	def start(self):
		client_obj = Needle()
		client_obj.listen()

	def stop(self):
		pass
