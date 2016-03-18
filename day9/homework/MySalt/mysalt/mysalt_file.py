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
from core import parse_file
loger = logging.getLogger(__name__)


# 发送文件
def sftp_put(ip, localpath, remotepath):
	transport = paramiko.Transport(ip, 22)
	transport.connect(username="root", password="rootroot")
	sftp = paramiko.SFTPClient.from_transport(transport)
	# 上传文件
	sftp.put(localpath, remotepath)
	transport.close()


# 接收文件
def sftp_get(ip, remotepath, localpath):
	transport = paramiko.Transport(ip, 22)
	transport.connect(username="root", password="rootroot")
	sftp = paramiko.SFTPClient.from_transport(transport)
	# 下载文件
	sftp.get(remotepath, localpath)
	transport.close()


def get(arg):
	print("This is the func of get file from remote path.")
	# pool = Pool(5)
	if len(arg) != 2:
		loger.info("Lack of arguments.acquired arg:{}".format(arg))
	else:
		obj_list, file_list = arg
		ip_list = handler.myhandler(obj_list)
		src_dst_list = parse_file.parse_file("get", file_list)
		for i in ip_list:
			for j in src_dst_list:
				sftp_get(i, j[0], j[1])
				# pool.apply_async(sftp_get, args=(i, j[0], j[1]))
				loger.info("get {} from {}.".format(j[0], j[1]))
		# pool.close()
		# pool.join()


def put(arg):
	print("This is the func of put file to remote path.")
	# pool = Pool(5)
	if len(arg) != 2:
		loger.info("Lack of arguments.acquired arg:{}".format(arg))
	else:
		obj_list, file_list = arg
		ip_list = handler.myhandler(obj_list)
		src_dst_list = parse_file.parse_file("put", file_list)
		for i in ip_list:
			for j in src_dst_list:
				sftp_put(i, j[0], j[1])
				# pool.apply_async(sftp_get, args=(i, j[0], j[1]))
				loger.info("put {} from {}.".format(j[0], j[1]))
		# pool.close()
		# pool.join()
