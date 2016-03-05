#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import socket

ip_port = ("127.0.0.1", 44444)

client = socket.socket()
client.connect(ip_port)

while True:
	data = input("==>").strip()
	msg = bytes(data, "utf8")
	client.send(msg)
	request = client.recv(1024)
	print("Server reply:{}".format(request.decode()))
