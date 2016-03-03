#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
FTP Server端
"""

import os
import sys
import socketserver
import subprocess
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting
from core import db_handler


class MyServer(socketserver.BaseRequestHandler):

	login_flag = False
	name = None
	home_path = None
	curr_path = None

	def handle(self):
		print("Server waiting...")
		conn = self.request
		conn.sendall(b"Welcome to qimi FTP....")
		flag = True
		while flag:
			command_msg = conn.recv(1024)
			try:
				str_command = str(command_msg.decode()).strip()
				print(str_command)
				# 传过来的命令按空格分割，保存到一个列表
				command_list = str_command.split()
				print(command_list)
				# 第一个参数是命令类型
				command = command_list[0].strip()
				print(command)
				# 如果有这个方法就执行
				if hasattr(self, command):
					func = getattr(self, command)
					func(str_command)
				# 没有就返回提示信息
				else:
					conn.send(b"Unknown command,Please retry...")
			except UnicodeDecodeError as e:
				print("decode error!", e)
				continue
			except Exception:
				print("unknown error")
				continue

	def login(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 3:
			username = command_list[1]
			password = command_list[2]
			accounts_db = db_handler.handler(setting.DATABASE)
			if username in accounts_db:
				if password == accounts_db[username]["password"]:
					self.login_flag = True
					self.name = username
					self.home_path = accounts_db[username]["home_path"]
					self.curr_path = accounts_db[username]["home_path"]
				else:
					self.login_flag = False
			else:
				self.login_flag = False
		else:
			self.login_flag = False
		if self.login_flag:
			self.request.sendall(b"Login success.")
		else:
			self.request.sendall(b"Login failed.")

	# 查看
	def show(self, str_command):
		conn = self.request
		command = "ls {}/{}".format(setting.BASE_DIR, self.curr_path)
		result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		result_msg = result.stdout.read()
		result_msg_size = len(result_msg)
		result_msg_info = bytes("SHOW_RESULT_SIZE|{}".format(result_msg_size), "utf8")
		conn.send(result_msg_info)
		recv_msg = conn.recv(100)
		if recv_msg.decode() == "CLIENT_READY_TO_RECEIVE":
			print("start to send data...")
			conn.send(result_msg)

	# 下载
	def get(self, str_command):
		conn = self.request
		command_list = str_command.split()
		print(command_list)
		if len(command_list) == 2:
			file_name = command_list[1]
			file_path = "{}/{}/{}".format(setting.BASE_DIR, self.curr_path, file_name)
			print(file_path)
			if os.path.isfile(file_path):
				file_size = os.path.getsize(file_path)
				print(file_size)
				file_info = "FILE_NAME:{}|FILE_SIZE:{}".format(file_name, file_size)
				file_info_msg = bytes(file_info, "utf8")
				print(file_info_msg)
				conn.send(file_info_msg)
				recv_msg = conn.recv(100)
				if recv_msg.decode() == "CLIENT_READY_TO_RECEIVE":
					print("start to send data ...")
					with open(file_path, "rb") as f:
						bytes_data = f.read(1024)
						# 有数据就一直传
						while bytes_data:
							conn.send(bytes_data)
							bytes_data = f.read(1024)
						else:
							print("=====send done!=====")
			else:
				conn.send(b"NO_THIS_FILE")

	# 上传
	def put(self, str_command):
		conn = self.request
		file_info_msg = conn.recv(100)
		try:
			info_list = str(file_info_msg.decode()).split("|")
			bool_a = info_list[0].split(":")[0] == "FILE_NAME"
			bool_b = info_list[1].split(":")[0] == "FILE_SIZE"
			if all([bool_a, bool_b]):
				file_name = info_list[0].split(":")[1]
				file_size = int(info_list[1].split(":")[1])
				print("要接收的文件是：{}，文件大小：{}".format(file_name, file_size))
				# 给server端发送一个回执，准备好开始接收文件
				conn.send(b"SERVER_READY_TO_RECEIVE")
				# 定义一个变量：存储已接收的数据大小
				recv_size = 0
				# 打开文件
				with open(file_name, "ab") as f:
					# 只要已接收的数据小于文件大小就一直接收
					while recv_size < file_size:
						# 接收文件数据
						bytes_data = conn.recv(1024)
						recv_size += len(bytes_data)
						f.write(bytes_data)
					else:
						print("==========receive done==========")
		except TypeError:
			pass
		except Exception:
			print("Error!")

	# 改变路径
	def cd(self, str_command):
		conn = self.request
		command_list = str_command.split()
		if command_list[1].startswith(self.home_path):
			conn.send(b"CHANGE_DIR_OK")
		else:
			conn.send(b"PERMISSION_DENIED")


if __name__ == "__main__":

	server = socketserver.ThreadingTCPServer(("127.0.0.1", 4444), MyServer)
	server.serve_forever()
