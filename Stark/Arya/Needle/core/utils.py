#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com


"""

"""


class MsgPrint(object):

	@staticmethod
	def error(msg, exit_flag=True):
		msg = "\033[31;1mError:\033[0m{}".format(msg)
		print(msg)

		if exit_flag:
			exit()
