#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
实现socket传文件的服务端
因为发送的文件大小未知，所以会出现各种问题
解决思路就是：先发送文件大小给对方，对方收到后给个（已准备好接收文件的）回执，然后这边开始发送文件
对端直到接收的文件大小与开始收到的大小相同时，则此次传输成功。
注意：该代码在中文操作系统下转str会有问题。
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
    conn.send(b"Please login...")
    while True:
        client_data = conn.recv(1024)
        if not client_data:
            break
        else:
            str_client_data = str(client_data, "utf8").strip()
            if str_client_data == "ok":
                file_path = '/home/qimi/src/Python-3.5.1.tgz'
                data_size = os.stat(file_path).st_size
                data_name = os.path.basename(file_path)
                send_msg = bytes("FILE_NAME:{}|FILE_SIZE:{}".format(data_name, data_size), "utf8")
                conn.send(send_msg)
                recv_data = conn.recv(100)
                if recv_data.decode() == "CLIENT_READY_TO_RECEIVE":
                    print("start to send data ...")
                    with open(file_path, "rb") as f:
                        n = 1
                        bytes_data = f.read(1024)
                        print("{}:{}".format(n, len(bytes_data)))
                        while bytes_data:
                            conn.send(bytes_data)
                            print(n)
                            print(f.tell())
                            n += 1
                            bytes_data = f.read(1024)
                        else:
                            print("=====send done!=====")

    server.close()
