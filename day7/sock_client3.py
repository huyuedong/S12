#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket 客户端
"""

import socket

ip_port = ('127.0.0.1', 4444)
sk = socket.socket()
sk.connect(ip_port)

while True:
	send_data = input("cmd:").strip()
	send_data = bytes(send_data, 'utf8')
	sk.send(send_data)
	recv_data = sk.recv(1024)
	print(type(recv_data))
	print(str(recv_data.decode()))
sk.close()
