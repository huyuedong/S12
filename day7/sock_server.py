#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket server 端
"""

import socket

ip_port = ('127.0.0.1', 4444)

sk = socket.socket()

sk.bind(ip_port)

sk.listen(5)

while True:
	print("Server waiting...")
	conn, addr = sk.accept()
	client_data = conn.recv(1024)
	print(str(client_data, "utf-8"))
	conn.sendall(bytes("不要回答，不要回答，不要回答！", 'utf-8'))
	conn.close()
