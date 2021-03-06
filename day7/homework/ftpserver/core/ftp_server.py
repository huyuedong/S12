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
import hashlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting
from core import db_handler


class MyServer(socketserver.BaseRequestHandler):

	login_flag = False
	name = None
	# 家目录
	home_path = None
	# 当前目录
	curr_path = None
	# 总磁盘配额
	total_space = None
	# 当前磁盘配额
	curr_space = None

	def handle(self):
		print("Server waiting...")
		conn = self.request
		conn.sendall(b"This is qimi's FTP, please login....")
		flag = True
		while flag:
			command_msg = conn.recv(1024)
			if not command_msg:
				flag = False
			else:
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
				except KeyboardInterrupt:
					flag = False
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
					# 获取用户家目录
					self.home_path = accounts_db[username]["home_path"]
					# login之后，当前目录默认为家目录
					self.curr_path = accounts_db[username]["home_path"]
					# 从数据库中读取用户的磁盘配额
					self.total_space = accounts_db[username]["total_space"]
					# 计算用户已使用的磁盘配额
					usage_space = os.path.getsize("{}/{}".format(setting.BASE_DIR, self.home_path))
					# 得到用户当前可用的磁盘配额
					self.curr_space = self.total_space - usage_space

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
		command_list = str_command.split()
		command = "ls {}/{}".format(setting.BASE_DIR, command_list[1])
		result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		result_msg = result.stdout.read()
		result_msg_size = len(result_msg)
		if result_msg_size == 0:
			conn.send(bytes("It is empty under < {} >.".format(command_list[1]), "utf8"))
		else:
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
						m1 = hashlib.md5()
						bytes_data = f.read(1024)
						# 有数据就一直传
						while bytes_data:
							m1.update(bytes_data)
							conn.send(bytes_data)
							bytes_data = f.read(1024)
						else:
							get_msg = conn.recv(100)
							str_get_msg = str(get_msg.decode())
							if str_get_msg == "GET_FILE_MD5":
								str_md5 = m1.hexdigest()
								print(str_md5)
								conn.send(bytes("MD5|{}".format(str_md5), "utf8"))
								recv_msg2 = conn.recv(100)
								if str(recv_msg2.decode()) == "CHECK_SUCCESS":
									print("=====send done!=====")
								elif str(recv_msg2.decode()) == "CHECK_FAILED":
									print("md5 value of the file has change during the transmission.")
				# 如果返回断点续传，就进入断点续传模式
				elif recv_msg.decode() == "BREAKPOINT_RESUME":
					print("begin to breakpoint resume!")
					temp_file_md5_msg = conn.recv(100)
					str_temp_file_md5 = str(temp_file_md5_msg.decode())
					if str_temp_file_md5.startswith("MD5|"):
						if len(str_temp_file_md5.split("|")) == 2:
							temp_file_md5 = str_temp_file_md5.split("|")[1]
							with open(file_path, "rb") as f2:
								# 定义一个匹配到md5值的标签
								begin_flag = False
								m2 = hashlib.md5()
								bytes_data2 = f2.read(1024)
								while bytes_data2:
									m2.update(bytes_data2)
									bytes_data2 = f2.read(1024)
									# 如果找到md5值，则开始续传
									if m2.hexdigest() == temp_file_md5:
										begin_flag = True
									# 找到对应的md5值就开始发数据
									elif begin_flag:
										conn.send(b"BREAKPOINT_CONSUME_OK")
										# recv_msg3 = conn.recv(100)
										# str_recv_msg3 = str(recv_msg3.decode())
										# if str_recv_msg3 == ""
										conn.send(bytes_data2)
									else:
										continue
								# 循环结束了还是没有匹配到md5值，则断点续传失败。
								if not begin_flag:
									conn.send(b"BREAKPOINT_CONSUME_FAILED")
									print("md5 check failed!")
								else:
									str_md5 = m2.hexdigest()
									conn.send(bytes("MD5|{}".format(str_md5), "utf8"))
									recv_msg2 = conn.recv(100)
									if str(recv_msg2.decode()) == "CHECK_SUCCESS":
										print("=====send done!=====")
									elif str(recv_msg2.decode()) == "CHECK_FAILED":
										print("md5 value of the file has change during the transmission.")

				# 返回传输取消，则打印传输取消
				elif recv_msg.decode() == "TRANSMISSION_CANCEL":
					print("Transmission cancel!")
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
				# 如果上传的文件小于可用磁盘空间，则准备接收上传的文件
				if file_size < self.curr_space:
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
				else:
					# 文件大于可用磁盘空间时，发送空间不足的回执
					conn.send(b"OUT_OF_SPACE")

		except TypeError:
			pass
		except Exception:
			print("Error!")

	# 改变路径
	def cd(self, str_command):
		conn = self.request
		command_list = str_command.split()
		if command_list[1].startswith(self.home_path):
			if os.path.isdir("{}/{}".format(setting.BASE_DIR, command_list[1])):
				conn.send(b"CHANGE_DIR_OK")
			else:
				conn.send(bytes("Change directory failed,< {} > is not a valid directory".format(command_list[1]), "utf8"))
		else:
			conn.send(bytes("Change directory failed,permission denied!".format(command_list[1]), "utf8"))


def run():
	server = socketserver.ThreadingTCPServer(("127.0.0.1", 4444), MyServer)
	server.serve_forever()

if __name__ == "__main__":
	run()

