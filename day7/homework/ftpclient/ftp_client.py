#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
FTP Client
"""

import socket
import os
import sys
import time


class MyClient(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.client = socket.socket()
		self.client.connect((host, port))
		welcome_msg = self.client.recv(1024)
		print(str(welcome_msg.decode()))
		if self.login():
			self.menu()

		# 登录
	def login(self):
		username = input("username:").strip()
		password = input("password:").strip()
		send_msg = "login {} {}".format(username, password)
		self.client.send(bytes(send_msg, "utf8"))
		reply_msg = self.client.recv(1024)
		if str(reply_msg.decode()).strip() == "Login success.":
			print(str(reply_msg, "utf8"))
			base_dir = os.path.dirname(os.path.abspath(__file__))
			self.store_path = "{}/home".format(base_dir)
			self.name = username
			self.curr_path = username
			return True

	# 菜单
	def menu(self):
		exit_flag = False
		while not exit_flag:
			str_command = input("==>").strip()
			command_list = str_command.split()
			command = command_list[0]
			if command == "exit":
				exit_flag = True
			elif hasattr(self, command):
				func = getattr(self, command)
				func(str_command)
			else:
				print("Unknown command,Please retry!")

	def show(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 1:
			if command_list[0] == "show":
				self.client.send(bytes(str_command, "utf8"))
				recv_msg = self.client.recv(100)
				str_recv_msg = str(recv_msg.decode()).strip()
				if str_recv_msg.split("|")[0] == "SHOW_RESULT_SIZE":
					result_size = int(str_recv_msg.split("|")[1])
					self.client.send(b"CLIENT_READY_TO_RECEIVE")
					result = ""
					recv_size = 0
					while recv_size < result_size:
						result_data = self.client.recv(500)
						recv_size += len(result_data)
						result += str(result_data.decode())
					else:
						print(result)

	# 下载
	def get(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 2:
			self.client.send(bytes(str_command, "utf8"))
			# 接收server端发来的文件信息
			file_info = self.client.recv(1024)
			if str(file_info.decode()) == "NO_THIS_FILE":
				print("There is no file named {}".format(command_list[1]))
			try:
				info_list = str(file_info.decode()).split("|")
				bool_a = info_list[0].split(":")[0] == "FILE_NAME"
				bool_b = info_list[1].split(":")[0] == "FILE_SIZE"
				if all([bool_a, bool_b]):
					file_name = info_list[0].split(":")[1]
					file_size = int(info_list[1].split(":")[1])
					print("要接收的文件是：{}，文件大小：{}".format(file_name, file_size))
					# 给server端发送一个回执，准备好开始接收文件
					self.client.send(b"CLIENT_READY_TO_RECEIVE")
					file_path = "{}/{}".format(self.store_path, file_name)
					# 定义一个变量：存储已接收的数据大小
					recv_size = 0
					# 打开文件
					with open(file_path, "ab") as f:
						# 只要已接收的数据小于文件大小就一直接收
						while recv_size < file_size:
							# 接收文件数据

							bytes_data = self.client.recv(1024)
							recv_size += len(bytes_data)
							f.write(bytes_data)
							self.process_bar(recv_size, file_size)
						else:
							print("\nreceive done")
			except TypeError:
				pass
			except Exception:
				print("Error!")

	# 上传
	def put(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 2:
			file_name = command_list[1]
			file_size = os.stat(file_name).st_size
			file_info = "FILE_NAME:{}|FILE_SIZE:{}".format(file_name, file_size), "utf8"
			file_info_msg = bytes(file_info, "utf8")
			self.client.send(file_info_msg)
			recv_msg = self.client.recv(100)
			if recv_msg.decode() == "SERVER_READY_TO_RECEIVE":
				print("start to send data ...")
				with open(file_name, "rb") as f:
					send_size = 0
					bytes_data = f.read(1024)
					# 有数据就一直传
					while bytes_data:
						send_size += len(bytes_data)
						self.process_bar(send_size, file_size)
						self.client.send(bytes_data)
						bytes_data = f.read(1024)
					else:
						print("=====send done!=====")

	# 切换目录
	def cd(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 2:
			self.client.send(bytes(str_command, "utf8"))
			recv_msg = self.client.recv(100)
			if str(recv_msg.decode()) == "CHANGE_DIR_OK":
				self.curr_path = command_list[1]
			elif str(recv_msg.decode()) == "PERMISSION_DENIED":
				print("change directory failed, permission denied!")

	# 进度条
	def process_bar(self, start, end, width=50):
		"""
		打印进度条。。。
		:param start: 当前数据量
		:param end: 总数据量
		:param width: 总的进度条长度
		:return:
		"""
		# 当前百分数
		str_num = "{:.2f}%".format(start/end*100)
		# 当前要打印“#“的个数
		front = int(start * width / end)
		front_tag = "#" * front
		end_tag = " " * (width - front)
		tag = "{}{}".format(front_tag, end_tag)
		# 生成当前的进度条
		str_tag = "{:<7} [{}] {:,}\r".format(str_num, tag, end)
		# 打印当前进度条
		sys.stdout.write(str_tag)
		sys.stdout.flush()
		time.sleep(0.1)
		# 如果进度完成，则打印换行
		if len(str_tag) == width:
			sys.stdout.write("\n")
			sys.stdout.flush()

	# 帮助
	def help(self, str_command):
		print('''
		input:help            to get help info
		input:get filename    to download file from ftp server
		input:put filename    to upload file to ftp server
		input:exit            to exit the system
		input:show            to show the files in current directory
		input:cd directory    to change the current directory
		input:del filename    to delete file on ftp server
		''')

if __name__ == "__main__":
	myclient = MyClient("127.0.0.1", 4444)
