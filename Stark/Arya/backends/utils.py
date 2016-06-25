#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


from Arya import action_list
from Arya import models

import django
django.setup()


class ArgvManagement(object):
	"""
		接收用户指令，并分发指令到指定模块
	"""

	def __init__(self, argvs):
		self.argvs = argvs
		self.argv_parse()

	@staticmethod
	def help_msg():
		print("==-Available modules-==")
		for registered_module in action_list.actions:
			print("  {}".format(registered_module))
		exit()

	def argv_parse(self):
		if len(self.argvs) < 2:
			self.help_msg()
		module_name = self.argvs[1]
		if "." in module_name:
			module_name, mod_method = module_name.split(".")
			module_instance = action_list.actions.get(module_name)
			if module_instance:
				module_instance(self.argvs, models)

		else:
			exit("invalid module name argument.")
