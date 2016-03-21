#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用twisted 接收文件的客户端
notice:Python2.x
"""

import optparse

from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
	usage = """
	%prog [options] [hostname]:port ...
	"""

	parser = optparse.OptionParser(usage)

	_, address = parser.parse_args()

	if not address:
		print(parser.format_help())
		parser.exit()

	def parse_address(addr):
		if ":" not in addr:
			host = "127.0.0.1"
			port = addr
		else:
			host, port = addr.split(":", 1)

		if not port.isdigit():
			parser.error("Ports must be integers.")
		return host, int(port)
	return map(parse_address, address)


class PoetryProtocol(Protocol):
	poem = ""

	def dataReceived(self, data):
		self.poem += data

	def connectionLost(self, reason):
		self.poemReceived(self.poem)

	def poemReceived(self, poem):
		self.factory.poem_finished(poem)


class PoetryClientFactory(ClientFactory):

	protocol = PoetryProtocol

	def __init__(self, callback):
		self.callback = callback

	def poem_finished(self, poem):
		self.callback(poem)


def get_poetry(host, port, callback):
	"""

	:param host:
	:param port:
	:param callback:
	:return:
	"""
	from twisted.internet import reactor
	factory = PoetryClientFactory(callback)
	reactor.connectTCP(host, port, factory)


def poetry_main():
	addresses = parse_args()
	from twisted.internet import reactor

	poems = []

	def got_poem(poem):
		poems.append(poem)
		if len(poems) == len(addresses):
			reactor.stop()

	for address in addresses:
		host, port = address
		get_poetry(host, port, got_poem)

	reactor.run()

	for poem in poems:
		print(poem)

if __name__ == "__main__":
	poetry_main()
