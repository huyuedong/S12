#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
用协程实现的多并发socket服务端
通过gevent实现单线程下的多socket并发
"""

import sys
import time
import gevent
import socket

from gevent import monkey
monkey.patch_all()


def server(port):
	s = socket.socket()
	s.bind(('127.0.0.1', port))
	s.listen(500)
	while True:
		cli, addr = s.accept()
		gevent.spawn(handler_request, cli)


def handler_request(s):
	try:
		data = s.recv(1024)
		print("send by client:", data)
		s.send(data)
		if not data:
			s.shutdown(socket.SHUT_WR)
	except Exception as ex:
		print(ex)
	finally:
		s.close()

if __name__ == "__main__":
	server(4444)


