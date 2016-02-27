#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket client 端
"""

import socket

ip_port = ('127.0.0.1', 4444)

sk = socket.socket()
sk.connect(ip_port)

sk.sendall(bytes("请求占领地球！", 'utf-8'))

server_reply = sk.recv(1024)
print(str(server_reply, 'utf-8'))

sk.close()
