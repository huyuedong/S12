#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用select实现的伪同时处理多个socket客户端请求：客户端
source:https://pymotw.com/3/select/
"""

import socket
import sys

# 定义一个消息列表
message_list = [
	"This is the message.",
	"It will be sent ",
	"in parts.",
]

# 服务器的IP和端口信息
server_ip_port = ("127.0.0.1", 4444)

# 生成一堆socket实例
client_list = [
	socket.socket(),
	socket.socket(),
	# socket.socket(),
	# socket.socket(),
]

print("Connecting to {} port {}.".format(*server_ip_port), file=sys.stderr)

# 将socket连接实例分别去连接server端
for c in client_list:
	c.connect(server_ip_port)

# 将消息列表中的信息循环发送给server端
for message in message_list:
	outgoing_data = message.encode()
	for c in client_list:
		print("{}: sending {!r}.".format(c.getsockname(), outgoing_data), file=sys.stderr)
		c.send(outgoing_data)

	# 同时也接收server端返回的数据
	for c in client_list:
		data = c.recv(1024)
		print("{}: received {!r}.".format(c.getsockname(), data), file=sys.stderr)
		# 如果数据为空就关闭该连接
		if not data:
			print("Closing socket:{}".format(c.getsockname()), file=sys.stderr)
			c.close()
