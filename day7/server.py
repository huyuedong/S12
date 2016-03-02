#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
传文件的服务端
"""

import socket
import os

ip_port = ('127.0.0.1', 5444)
server = socket.socket()
server.bind(ip_port)
server.listen(5)

while True:
	print("Server waiting...")
	conn, addr = server.accept()
	# 给客户端发送请求登录的消息
	conn.send(b"Please login...")
	while True:
		# 接收客户端回应
		client_data = conn.recv(1024)
		if not client_data:
			break
		else:
			str_client_data = str(client_data, "utf8").strip()
			# 如果客户端回复ok,则发送要传输的文件名和文件大小
			if str_client_data == "ok":
				file_path = '/home/qimi/src/Python-3.5.1.tgz'
				data_size = os.stat(file_path).st_size
				data_name = os.path.basename(file_path)
				send_msg = bytes("FILE_NAME:{}|FILE_SIZE:{}".format(data_name, data_size), "utf8")
				conn.send(send_msg)
				# 等待客户端确认
				recv_data = conn.recv(100)
				# 如果客户端发送了准备接收数据，则开始传输数据
				if recv_data.decode() == "CLIENT_READY_TO_RECEIVE":
					print("start to send data...")
					# 以二进制打开文件
					with open(file_path, "rb") as f:
						# 一次读取1024
						bytes_data = f.read(1024)
						# 有数据就发送
						while bytes_data:
							conn.send(bytes_data)
							bytes_data = f.read(1024)
						#
						else:
							print("data send over!")

	server.close()

