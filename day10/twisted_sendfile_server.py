#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用twisted 发送文件的服务端
"""

import optparse
import os
from twisted.internet.protocol import ServerFactory, Protocol

def parse_args():
	usage = """
	usage %prog [options] poetry-file
	This is the Fast Poetry Server, Twisted edition.
	Run it like this:
		python fastpoetry.py <path-to-poetry-file>
	If you are in the base directory of the twisted-intro package,
	you could run it like this:
		python twisted-server-1/fastpoetry.py poetry/ecstasy.txt
	to serve up John Donne's Ecstasy, which I know you want to do.
	"""

	parser = optparse.OptionParser(usage)

	help = "The port to listen on.Default to a random available port"
	parser.add_option("--port", type="int", help=help)

	help = "The interface to listen on. Default is localhost."
	parser.add_option("--iface", help=help, default="localhost")

	options, args = parser.parse_args()
	print("arg==>:", options, args)

	# 必须要指定一个要传的文件参数
	if len(args) != 1:
		parser.error("Provide exactly one poetry file.")

	poetry_file = args[0]
	# 如果不存在那个文件就打印提示信息
	if not os.path.isfile(args[0]):
		parser.error("No such file:{}.".format(poetry_file))
	# 返回执行的参数和要发的文件
	return options, poetry_file

class PoetryProtocol(Protocol):

	def connectionMade(self):
		self.transport.write(self.factory.poem)
