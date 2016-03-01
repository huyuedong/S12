#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
用于连接SocketServer模块实现多线程的server端的client端
一直向服务端发数据，直到输入exit退出
"""

import socket


ip_port = ('127.0.0.1', 4444)

# 实例化客户端对象
client = socket.socket()
# 连接
client.connect(ip_port)
start_data = client.recv(1024)
print(str(start_data, "utf8"))

flag = True
while flag:
	send_data = input("==>").strip()
	if send_data == "exit":
		flag = False
	else:
		client.send(bytes(send_data, "utf8"))
		server_reply = client.recv(1024)
		print(str(server_reply, "utf8"))

client.close()
