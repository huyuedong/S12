#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
socket 客户端
"""
import socket

ip_port = ('127.0.0.1', 5444)
client = socket.socket()
client.connect(ip_port)

while True:
    recv_data = client.recv(100)
    print(recv_data.decode())
    while True:
        send_data = input("answer:").strip()
        if len(send_data) == 0:
            continue
        elif send_data == "q":
            break
        else:
            send_data = bytes(send_data, "utf8")
            client.send(send_data)
            recv_msg = client.recv(100)
            try:
                msg_list = str(recv_msg.decode()).split("|")
                a = msg_list[0].split(":")[0] == "FILE_NAME"
                b = msg_list[1].split(":")[0] == "FILE_SIZE"
                if all([a, b]):
                    file_name = msg_list[0].split(":")[1]
                    file_size = int(msg_list[1].split(":")[1])
                    print("要发送得文件名是：{}，文件大小：{}".format(file_name, file_size))
                    client.send(b"CLIENT_READY_TO_RECEIVE")
                    recv_size = 0
                    with open(file_name, "ab") as f:
                        while recv_size < file_size:
                            bytes_data = client.recv(1024)
                            recv_size += len(bytes_data)
                            print(recv_size)
                            f.write(bytes_data)
                        else:
                            print("==========receive done==========")
                else:
                    break
            except TypeError:
                pass
            except Exception:
                print("Error!")

    client.close()

