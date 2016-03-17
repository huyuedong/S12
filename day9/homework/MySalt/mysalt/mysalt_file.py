#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
The file execution module
"""

import paramiko
import os
import sys
import logging
from multiprocessing import Pool
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import handler
loger = logging.getLogger(__name__)


def get(arg):
	print("This is the func of get file from remote path.")
	pool = Pool(5)
	if len(arg) != 2:
		loger.info("Lack of arguments.acquired arg:{}".format(arg))
	else:
		obj_list, cmd_list = arg
		ip_list = handler.myhandler(obj_list)
		cmd = " ".join(cmd_list)
		for i in ip_list:
			pool.apply_async(sftp_get, args=(i, cmd))
		pool.close()
		pool.join()


def put(arg):
	print("This is the func of put file to remote path.")
	pool = Pool(5)
	if len(arg) != 2:
		loger.info("Lack of arguments.acquired arg:{}".format(arg))
	else:
		obj_list, cmd_list = arg
		ip_list = handler.myhandler(obj_list)
		cmd = " ".join(cmd_list)
		for i in ip_list:
			pool.apply_async(sftp_put, args=(i, cmd))
		pool.close()
		pool.join()


# 发送文件
def sftp_put(self, ip, localpath, remotepath):
	transport = paramiko.Transport(ip, 22)
	transport.connect(username="root", password="rootroot")
	sftp = paramiko.SFTPClient.from_transport(transport)
	# 上传文件
	sftp.put(localpath, remotepath)
	transport.close()


# 接收文件
def sftp_get(self, ip, remotepath, localpath):
	transport = paramiko.Transport(ip, 22)
	transport.connect(username="root", password="rootroot")
	sftp = paramiko.SFTPClient.from_transport(transport)
	# 下载文件
	sftp.get(remotepath, localpath)
	transport.close()
