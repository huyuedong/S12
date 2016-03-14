#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
利用select实现的伪同时处理多个socket客户端请求：服务端
source:https://pymotw.com/3/select/
"""

import select
import socket
import queue
import sys

# 生成一个socket实例
server = socket.socket()
# 设置为非阻塞
server.setblocking(False)
# 配置IP和端口
ip_port = ("127.0.0.1", 4444)
# 绑定IP和端口
server.bind(ip_port)

# 监听五个连接
server.listen(5)

# 生成一个readable的列表,用于存放所有输入的信息
inputs = [server, ]

# 生成一个writeable的列表，用于存放所有输出的信息
outputs = []

# 生成一个消息队列
message_queue = {}

while inputs:
	print("\nWaiting for the next event.", file=sys.stderr)
	# select返回三个列表，readable中存放可以接收数据的连接，writeable存放可以发送数据的连接，exceptional存放发生错误的连接
	readable, writeable, exceptional = select.select(inputs, outputs, inputs)

	# 处理可以读取的连接
	for s in readable:
		# 如果server在inputs列表里，表示server已经准备好接收连接请求
		if s is server:
			# 接收连接请求
			conn, addr = s.accept()
			# 打印提示信息
			print("A new collection from:", addr, file=sys.stderr)
			# 将该连接设为非阻塞
			conn.setblocking(0)
			# 在inputs列表中放入该连接
			inputs.append(conn)
			# 为每个连接生成一个消息队列，用于存放我们要发送给该连接的数据
			message_queue[conn] = queue.Queue()
		# 不是server就是具体的连接
		else:
			# 接收数据
			data = s.recv(1024)
			# 如果数据存在
			if data:
				# 打印可能出现的错误信息
				print("Received {!r} from {}.".format(data, s.getpeername()), file=sys.stderr)
				# 将收到的数据存放到以该连接为key值的消息队列中
				message_queue[s].put(data)
				# 如果该连接不在可以输出消息的socket连接列表中
				if s not in outputs:
					# 把该连接加入到可以输出消息的socket连接列表中
					outputs.append(s)
			# 如果没有数据就关闭连接
			else:
				print("Closing {} ,after reading no data.".format(addr), file=sys.stderr)
				# 该连接如果存在于可以输出消息的socket连接列表中，就删除
				if s in outputs:
					outputs.remove(s)
				# 也无需继续等待该连接的输入
				inputs.remove(s)
				# 关闭该连接
				s.close()
				# 从消息队列中删除该连接的消息
				del message_queue[s]

	# 处理输出的
	for s in writeable:
		try:
			next_msg = message_queue[s].get_nowait()
		# 如果消息队列为空
		except queue.Empty:
			# 打印提示信息
			print("Output queue for {} is empty.".format(s.getpeername()), file=sys.stderr)
			# 从可输出信息的socket连接列表中删除该连接
			outputs.remove(s)
		# 如果消息队列里有信息就将该信息发出。
		else:
			# 打印提示信息
			print("Sending {!r} to {}.".format(next_msg, s.getpeername()), file=sys.stderr)
			s.send(next_msg)
	# 处理异常情况
	for s in exceptional:
		# 打印提示信息
		print("Exceptional condition for {}.".format(s.getpeername()), file=sys.stderr)
		# 不再监听该连接是否可读
		inputs.remove(s)
		# 也不再监听是否可以对该连接发送数据
		if s in outputs:
			outputs.remove(s)
		# 关闭连接
		s.close()

		# 删除该连接的消息队列
		del message_queue[s]
