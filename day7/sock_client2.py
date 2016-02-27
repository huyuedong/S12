#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket client 端
"""

import socket

ip_port = ('127.0.0.1', 4444)

# 实例化客户端对象
sk = socket.socket()
# 连接
sk.connect(ip_port)
# 发送数据
sk.sendall(bytes("请求占领地球！", 'utf-8'))
# 接受服务端返回的数据
server_reply = sk.recv(1024)
# 将服务端返回的数据打印出来
print(str(server_reply, 'utf-8'))

# 创建一个一直获取输入的死循环，直到抛出异常是跳出
while True:
	# 获取输入
	recv_data = input("==>").strip()
	# 将输入的数据发给服务端
	sk.send(bytes(recv_data, 'utf-8'))
	# 获取服务端返回的数据
	server_reply = sk.recv(1024)
	# 将服务端返回的数据打印出来
	print(str(server_reply, 'utf-8'))

sk.close()
