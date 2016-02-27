#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket server 端
要client 端先断开，如果先断开server的话，端口还会被client端占用，要等到操作系统回收之后才能继续使用
"""

import socket

# 定义连接参数
ip_port = ('127.0.0.1', 4444)
# 实例化socket对象
sk = socket.socket()
# 绑定
sk.bind(ip_port)

sk.listen(5)

# 创建一个死循环，一直等待客户端的连接
while True:
	# 打印服务端等待的提示信息
	print("Server waiting...")
	# 接受连接
	conn, addr = sk.accept()
	# 接受客户端的数据
	client_data = conn.recv(1024)
	# 将接受的客户端的数据打印出来
	print(str(client_data, "utf-8"))
	# 将接受的客户端的数据返回给客户端
	conn.sendall(bytes("不要回答，不要回答，不要回答！", 'utf-8'))
	# 创建接受客户端信息的死循环，直到连接断开跳出
	while True:
		try:
			# 接受数据
			client_data = conn.recv(1024)
			# 打印数据
			print(str(client_data, 'utf-8'))
		except Exception:
			print("collection closed...")
			# 跳出
			break
		# 将接受的数据返回给客户端
		conn.send(client_data)
	conn.close()
