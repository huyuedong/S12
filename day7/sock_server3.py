#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
实现socket传文件的服务端
因为发送的文件大小未知，所以会出现各种问题
解决思路就是：先发送文件大小给对方，对方收到后给个（已准备好接收文件的）回执，然后这边开始发送文件
对端直到接收的文件大小与开始收到的大小相同时，则此次传输成功。
"""

import socket
import subprocess

ip_port = ('127.0.0.1', 4444)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
	print("server waiting...")
	conn, addr = sk.accept()
	while True:
		try:
			client_data = conn.recv(1024)
			if not client_data: continue
			str_client_data = str(client_data, 'utf8').strip()
			print("the cmd:{}".format(str_client_data))
			# 管道执行命令
			result = subprocess.Popen(str_client_data, shell=True, stdout=subprocess.PIPE)
			# 获取命令显示的结果
			result_data = result.stdout.read()
			print(type(result_data))
		except Exception:
			print("collection closed, break")
			break
		conn.send(result_data)
	sk.close()
