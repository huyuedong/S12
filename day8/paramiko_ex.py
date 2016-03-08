#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
paramiko练习
"""

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()

# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接服务器
ssh.connect(hostname="172.18.26.193", port=22, username="root", password="rootroot")

# 执行命令
stdin, stdout, stderr = ssh.exec_command("df")
result = stdout.read()

ssh.close()

print(result.decode())
