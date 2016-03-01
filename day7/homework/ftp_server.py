#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
FTP Server端
"""

import socket
import subprocess

ip_port = ('127.0.0.1', 5444)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
        print("server waiting...")
        conn, addr = sk.accept()
        while True:
                client_data = conn.recv(1024)
                if not client_data:break
                str_client_data = str(client_data, 'utf8').strip()
                print("the cmd:{}".format(str_client_data))
                # 管道执行命令
                result = subprocess.Popen(str_client_data, shell=True, stdout=subprocess.PIPE)
                # 获取命令显示的结果
                result_data = result.stdout.read()
                if len(result_data) == 0:
                    result_data = b'cmd execution has no output...'
                ack_msg = bytes("CMD_RESULT_SIZE|{}".format(len(result_data)), 'utf8')
                # 先发送数据大小
                conn.send(ack_msg)
                client_ack = conn.recv(50)
                if client_ack.decode() == "CLIENT_READY_TO_RECV":
                    conn.send(result_data)
        sk.close()

