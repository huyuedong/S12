#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
用协程实现的socket客户端
"""

import socket

host = "127.0.0.1"
port = 4444

s = socket.socket()
s.connect((host, port))
while True:
	msg = bytes(input("==>:"), encoding="utf8")
	# if len(msg) == 0:
	# 	continue
	s.sendall(msg)
	data = s.recv(1024)
	print("receive from server3:", data.decode())
s.close()
