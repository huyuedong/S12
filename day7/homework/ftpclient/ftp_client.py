#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
FTP Client
"""

import socket
import os
import sys
import getpass
import hashlib


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
		while True:
			username = input("username:").strip()
			password = getpass.getpass("password:").strip()
			send_msg = "login {} {}".format(username, password)
			try:
				self.client.send(bytes(send_msg, "utf8"))
				reply_msg = self.client.recv(1024)
				if str(reply_msg.decode()).strip() == "Login success.":
					base_dir = os.path.dirname(os.path.abspath(__file__))
					self.store_path = "{}/home".format(base_dir)
					self.name = username
					self.curr_path = "home/{}".format(username)
					print("Hi {}, welcome to login qimi's FTP.".format(self.name))

					return True
				else:
					print(str(reply_msg.decode()))
			except KeyboardInterrupt:
				break

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
				# 默认显示显示当前目录的文件
				str_command_msg = "{} {}".format(str_command, self.curr_path)
				self.client.send(bytes(str_command_msg, "utf8"))
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
						print("The directory < {} > has:".format(self.curr_path))
						print(result)
				else:
					print(str_recv_msg)

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
					temp_file_name = "{}.temp".format(file_name)
					file_size = int(info_list[1].split(":")[1])
					# 先将文件存为一个以.temp的临时文件
					temp_file_path = "{}/{}".format(self.store_path, temp_file_name)
					file_path = "{}/{}".format(self.store_path, file_name)
					# 如果本地没有这个文件，则准备接收
					if not os.path.isfile(file_path):
						print("要接收的文件是：{},文件大小：{}".format(file_name, file_size))
						# 给server端发送一个回执，准备好开始接收文件
						self.client.send(b"CLIENT_READY_TO_RECEIVE")
						# 定义一个变量：存储已接收的数据大小
						recv_size = 0
						# 打开文件
						with open(temp_file_path, "wb") as f:
							m1 = hashlib.md5()
							# 只要已接收的数据小于文件大小就一直接收
							while recv_size < file_size:
								# 接收文件数据
								bytes_data = self.client.recv(1024)
								m1.update(bytes_data)
								recv_size += len(bytes_data)
								f.write(bytes_data)
								self.process_bar(recv_size, file_size)
							else:
								self.client.send(b"GET_FILE_MD5")
								# 获取本地文件的md5值
								str_md5 = m1.hexdigest()
								# 接收server端文件的md5值
								recv_msg = self.client.recv(100)
								str_recv_msg = str(recv_msg.decode())
								if str_recv_msg.startswith("MD5|"):
									if len(str_recv_msg.split("|")) == 2:
										file_md5 = str_recv_msg.split("|")[1]
										# 如果本地文件的md5值与服务端文件的md5值相同，则传输成功
										if str_md5 == file_md5:
											# 像服务端发送md5验证通过消息
											self.client.send(b"CHECK_SUCCESS")
											os.rename(temp_file_path, file_path)
											print("\nreceive done!")
										# md5校验不一致
										else:
											self.client.send(b"CHECK_FAILED")
											os.remove(temp_file_path)
											print("File has changed during the transmission!")
					# 如果本地有该文件的临时文件，则进入断点续传
					elif os.path.isfile(temp_file_path):
						print("There is a temp file of {}, try to begin breakpoint resume!".format(file_name))
						self.client.send(b"BREAKPOINT_RESUME")
						with open(temp_file_path, "rb") as f2:
							m2 = hashlib.md5()
							temp_file_size = 0
							while temp_file_size < os.path.getsize(temp_file_path):
								bytes_data2 = f2.read(1024)
								m2.update(bytes_data2)
								temp_file_size += len(bytes_data2)
							else:
								# 发送本地文件md5值
								temp_file_md5 = m2.hexdigest()
								self.client.send(bytes("MD5|{}".format(temp_file_md5), "utf8"))
						recv_msg2 = self.client.recv(100)
						str_recv_msg2 = str(recv_msg2.decode())
						if str_recv_msg2 == "BREAKPOINT_CONSUME_OK":
							print("Begin to breakpoint consume.")
							recv_size2 = temp_file_size
							with open(temp_file_path, "ab") as f3:
								# 本地文件小于server端文件就一直收
								while recv_size2 < file_size:
									bytes_data3 = self.client.recv(1024)
									m2.update(bytes_data3)
									recv_size2 += len(bytes_data3)
									f3.write(bytes_data3)
									self.process_bar(recv_size2, file_size)
								else:
									# 获取本地文件的md5值
									str_md5 = m2.hexdigest()
									# 接收server端文件的md5值
									recv_msg = self.client.recv(100)
									str_recv_msg = str(recv_msg.decode())
									if str_recv_msg.startswith("MD5|"):
										if str_recv_msg.split("|") == 2:
											file_md5 = str_recv_msg.split("|")[1]
											# 如果本地文件的md5值与服务端文件的md5值相同，则传输成功
											if str_md5 == file_md5:
												# 像服务端发送md5验证通过消息
												self.client.send(b"CHECK_SUCCESS")
												os.rename(temp_file_path, file_path)
												print("\nreceive done!")
											# md5校验不一致
											else:
												self.client.send(b"CHECK_FAILED")
												os.remove(temp_file_path)
												print("File has changed during the transmission!")
						elif str_recv_msg2 == "BREAKPOINT_RESUME_FAILED":
							print("Breakpoint resume failed, delete local file and retry!")
					elif os.path.isfile(file_path):
						print("{} is already exist!".format(file_name))
						self.client.send(b"TRANSMISSION_CANCEL")
			except TypeError:
				pass
			except Exception:
				print("Error!")

	# 上传
	def put(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 2:
			file_name = command_list[1]
			# 需要上传的文件需要放在与ftpclient下的home目录
			file_path = "{}/{}".format(self.store_path, file_name)
			# 判断输入的文件名是否存在
			if os.path.isfile(file_path):
				# 发送上传文件的命令，触发server端的put()
				self.client.send(bytes(str_command, "utf8"))
				file_size = os.path.getsize(file_path)
				file_info = "FILE_NAME:{}|FILE_SIZE:{}".format(file_name, file_size)
				file_info_msg = bytes(file_info, "utf8")
				self.client.send(file_info_msg)
				recv_msg = self.client.recv(100)
				if recv_msg.decode() == "SERVER_READY_TO_RECEIVE":
					print("start to send data ...")
					with open(file_path, "rb") as f:
						send_size = 0
						bytes_data = f.read(1024)
						# 有数据就一直传
						while bytes_data:
							send_size += len(bytes_data)
							self.client.send(bytes_data)
							bytes_data = f.read(1024)
							self.process_bar(send_size, file_size)
						else:
							print("\nsend done!")
				elif recv_msg.decode() == "OUT_OF_SPACE":
					print("The server doesn't have enough space to receive this file. ")
			else:
				print("There is no files named < {} > in < {} >.".format(file_name, self.store_path))

	# 切换目录
	def cd(self, str_command):
		command_list = str_command.split()
		if len(command_list) == 2:
			self.client.send(bytes(str_command, "utf8"))
			recv_msg = self.client.recv(100)
			if str(recv_msg.decode()) == "CHANGE_DIR_OK":
				print("Changed current directory to < {} >.".format(command_list[1]))
				self.curr_path = command_list[1]
			else:
				print(str(recv_msg.decode()))

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

	# 帮助
	def help(self, str_command):
		print('''
		input:help            to get help info
		input:get filename    to download file from ftp server
		input:put filename    to upload file under < ftpclient/home/ > to ftp server
		input:exit            to exit the system
		input:show            to show the files in current directory
		input:cd directory    to change the current directory
		input:del filename    to delete file on ftp server
		''')

if __name__ == "__main__":
	myclient = MyClient("127.0.0.1", 4444)
