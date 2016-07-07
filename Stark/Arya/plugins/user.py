#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
处理user相关
"""

from Arya.backends.base_module import BaseSaltModule


class User(BaseSaltModule):

	def uid(self, *args, **kwargs):
		self.argv_validation("uid", args[0], int)
		cmd = "-u {}".format(args[0])
		self.raw_cmds.append(cmd)
		return cmd

	def gid(self, *args, **kwargs):
		pass

	def shell(self, *args, **kwargs):
		pass

	def home(self, *args, **kwargs):
		pass


class UbuntuUser(User):

	def home(self, *args, **kwargs):
		print("in ubuntu home...")
