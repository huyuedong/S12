#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import socketserver


class MySocketServerHandler(socketserver.BaseRequestHandler):
	def handle(self):
		print("New Connection:{}".format(self.client_address))
		while True:
			data = self.request.recv(1024)
			if not data:
				break
			msg = data.decode()
			print("Client said:{}".format(msg))
			self.request.send(data)

if __name__ == "__main__":
	ip = "127.0.0.1"
	port = 44444
	server = socketserver.ThreadingTCPServer((ip, port), MySocketServerHandler)
	server.serve_forever()
