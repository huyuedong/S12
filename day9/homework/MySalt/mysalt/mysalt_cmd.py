#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
the cmd execution module
mysalt "operate object" module.func "instruction"
arg = ["operate object", module.func, "instruction"]
"""
import paramiko
import os
import sys
import logging
from multiprocessing import Pool
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import handler
loger = logging.getLogger(__name__)


# 执行命令
def cmd_func(ip, cmd):
	# 创建SSH对象
	ssh = paramiko.SSHClient()
	# 允许连接不在know_hosts文件中的主机
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	# 连接服务器
	ssh.connect(hostname=ip, port=22, username="root", password="rootroot")
	# 执行命令
	stdin, stdout, stderr = ssh.exec_command(cmd)
	# result = stdout.read() if stdout.read() else stderr.read()
	result = list(filter(lambda t: t is not None, [stdout.read(), stderr.read()]))[0]
	ssh.close()
	print("IP:{} return==>:".format(ip))
	print(result.decode())


def run(arg):
	print("Execute the command in batch.")
	if len(arg) != 2:
		loger.info("Lack of arguments.acquired arg:{}".format(arg))
	else:
		obj_list, cmd_list = arg
		ip_list = handler.myhandler(obj_list)
		cmd = " ".join(cmd_list)
		if len(ip_list) >= 1:
			# pool = Pool(5)
			for i in ip_list:
				cmd_func(i, cmd)
				# pool.apply_async(cmd_func, args=(i, cmd))
			# pool.close()
			# pool.join()
		else:
			print("No host to connect.")
			loger.info("ip list is empty.")
