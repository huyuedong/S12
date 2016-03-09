#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
paramiko 练习
SFTPClient: 用于连接远程服务器并执行上传下载
"""

import paramiko

transport = paramiko.Transport(("192.168.183.131", 22))
transport.connect(username="root", password="rootroot")

sftp = paramiko.SFTPClient.from_transport(transport)

# 上传文件
# sftp.put("D:\\qimi_WorkSpace\\S12\\tab.py", "/home/qimi/python/tab.py")

# 下载文件
sftp.get("/home/qimi/python/tab.py", "D:\\qimi_WorkSpace\\S12\\tab2.py")

transport.close()

