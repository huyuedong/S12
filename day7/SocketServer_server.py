#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用SocketServer模块实现多线程的server端
"""

import socketserver


class MyServer(socketserver.BaseRequestHandler):

	# 必须覆写的方法
	def handle(self):
		conn = self.request
		conn.sendall(b"Please input the message:")
		flag = True
		while flag:
			try:
				data = conn.recv(1024)
				str_data = str(data.decode()).strip()
				if str_data == "exit":
					flag = False
				elif data:
					conn.send(data)
				else:
					conn.send(b"Please retry...")
			except Exception:
				continue

if __name__ == "__main__":
	server = socketserver.ThreadingTCPServer(("127.0.0.1", 4444), MyServer)
	server.serve_forever()
