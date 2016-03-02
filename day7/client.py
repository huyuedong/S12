#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
传文件的客户端
"""

import socket

ip_port = ('127.0.0.1', 5444)
client = socket.socket()
client.connect(ip_port)

while True:
	# 接收服务端发来的消息
	recv_data = client.recv(100)
	# 打印服务端发来的消息
	print(recv_data.decode())
	while True:
		# 获取输入
		send_data = input("answer:").strip()
		if len(send_data) == 0:
			continue
		elif send_data == "q":
			break
		else:
			send_data = bytes(send_data, "utf8")
			# 将客户端的输入发送给服务端
			client.send(send_data)
			# 准备接收服务端发来的文件信息
			recv_msg = client.recv(100)
			try:
				msg_list = str(recv_msg.decode()).split("|")
				a = msg_list[0].split(":")[0] == "FILE_NAME"
				b = msg_list[1].split(":")[0] == "FILE_SIZE"
				if all([a, b]):
					file_name = msg_list[0].split(":")[1]
					file_size = int(msg_list[1].split(":")[1])
					print("要接收的文件是：{}，文件大小：{}".format(file_name, file_size))
					client.send(b"CLIENT_READY_TO_RECEIVE")
					recv_size = 0
					with open(file_name, "ab") as f:
						while recv_size < file_size:
							bytes_data = client.recv(1024)
							recv_size += len(bytes_data)
							f.write(bytes_data)
				else:
					print("==========receive done==========")
			except TypeError:
				pass
			except Exception:
				print("Error!")

	client.close()
