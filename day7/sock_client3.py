#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket 客户端
"""

import socket

ip_port = ('127.0.0.1', 5444)
sk = socket.socket()
sk.connect(ip_port)

while True:
        send_data = input("cmd:").strip()
        if len(send_data) == 0:continue
        elif send_data == "q":break
        send_data = bytes(send_data, 'utf8')
        sk.send(send_data)
        cmd_res_msg = sk.recv(100)
        cmd_res_msg = str(cmd_res_msg.decode()).split("|")
        print("server response:{}".format(cmd_res_msg))
        if cmd_res_msg[0] == "CMD_RESULT_SIZE":
            cmd_res_size = int(cmd_res_msg[1])
            sk.send(b"CLIENT_READY_TO_RECV")
            # 定义一个空的字符串用于拼接接收到的数据
            res = ""
            # 已经接收的数据量
            received_size = 0
            # 当接受的数据量小于之前传过来的数据量的值时，一直接收数据
            while received_size < cmd_res_size:
                data = sk.recv(500)
                received_size += len(data)
                res += str(data.decode())
            else:
                print(str(res))
                print("==============recv done============")
sk.close()

