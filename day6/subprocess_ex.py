#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
subprocess模块的练习
"""

import subprocess

# subprocess.run("ipconfig")
#
# p = subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE)
# print(p.stdout.read())


# 需要交互的命令
obj = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
obj.stdin.write(b"print('hello1')\n")
obj.stdin.write(b"print('hello2')\n")
obj.stdin.write(b"print('hello3')\n")
a = obj.communicate(timeout=10)
print(a)

