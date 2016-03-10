#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
可以对机器进行分组
可以对指定的一组或多组机器执行批量命令，分发文件(发送\接收)
纪录操作日志
version: v0.1
"""

import os
import sys
import re
import getpass
import multiprocessing
import paramiko
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import config_handler
from conf import setting

loger = logging.getLogger(__name__)


class QClient(object):

	# 错误代码
	def __init__(self):
		self.response_code = {
			'200': "200...",
			'201': "201...",
			'202': "202...",
			'300': "300...",
			'301': "301...",
			'302': "302...",
		}
		self.login_name = None
		self.exit_flag = False
		if self.login():
			self.menu()

	# 主菜单
	def menu(self):
		print("This is a batch host management tool.")
		while not self.exit_flag:
			input_cmd = input("[{}]==>".format(self.login_name)).strip()
			self.instruction_parse(input_cmd)

	# 退出
	def exit(self, instructions):
		print("Bye~")
		loger.info("{} logout.".format(self.login_name))
		self.exit_flag = True

	# 查看主机分组
	def show(self, instructions):
		print("show group of host...")
		# 读取配置
		configure = config_handler.read()
		# 只有一个show的时候默认打印所有的组名
		if len(instructions) == 1:
			for k in configure:
				print("group:{}".format(k))
		elif "-g" in instructions:
			# 获取用户输入的组名
			group_name = instructions[instructions.index("-g") + 1]
			# 如果有这个组名，就遍历打印出这个组下的所有主机记录
			try:
				print("group:{}".format(group_name))
				for i in configure[group_name]:
					print(i)
					loger.info("{} checkout the host of the group:{}.".format(self.login_name, group_name))
			# 如果没有这个组，就打印提示信息。
			except (ValueError, KeyError):
				print("invalid group name!")
				loger.debug("{}=>:{}".format(self.login_name, instructions))
		# 命令错误打印提示
		else:
			print("invalid instructions!")
			self.instruction_msg()

	# 增加主机记录
	def add(self, instructions):
		print("add host record to the group...")
		add_flag = True
		# 参数小于5，就提示参数不足
		if len(instructions) < 5:
			print("Lack of arguments")
		else:
			mandatory_filed = ["-g", "-h"]
			for i in mandatory_filed:
				if i not in instructions:
					print("invalid instruction")
					add_flag = False
			if add_flag:
				index_g = instructions.index("-g")
				index_h = instructions.index("-h")
				# 得到用户输入的组名列表
				group_list = instructions[index_g+1:index_h]
				# 得到用户输入的主机名列表
				host_list = instructions[index_h+1:]
				# 判断host_list中的ip是否都是有效ip
				p = re.compile(r'^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$')
				flag_h = True
				for i in host_list:
					# 如果匹配到不合法的IP,就把flag_h置为False
					if not p.match(i):
						flag_h = False
				# 如果用户输入的全为合法IP，则增加记录
				if flag_h:
					configure = config_handler.read()
					for i in group_list:
						# 如果存在分组就将主机记录更新
						if i in configure.keys():
							configure.keys().append(host_list)
							loger.info("{} update hosts:{} in group:{}.".format(self.login_name, host_list, i))
						# 如果不存在该分组就新增
						else:
							print("There is no group named {},will you want to add?".format(i))
							option = input("Type [Y/y] to confirm, otherwise discard.").strip()
							# 新加分组需要确认
							if option.upper() == "Y":
								configure[i] = host_list
								config_handler.write(configure)
								loger.info("{} input {},and add a new group:{} hosts:{}".format(self.login_name, instructions, i, host_list))
							# 放弃修改就打印提示
							else:
								print("give up this operation.")
								loger.debug("{} input {}, and give up to add a group:() in this operation.".format(self.login_name, i))
				# 提示用户输入了无效的IP
				else:
					print("Your input instruction has some invalid IP.")
					loger.debug("{} input {}, and it has some invalid IP.")

	# 删除主机
	def delete(self, instructions):
		print("delete some hosts in the group,and the empty group will be delete. ")
		delete_flag = True
		configure = config_handler.read()
		if len(instructions) < 5:
			print("Lack of arguments")
		else:
			mandatory_filed = ["-g", "-h"]
			for i in mandatory_filed:
				if i not in instructions:
					print("invalid instruction")
					delete_flag = False
			if delete_flag:
				index_g = instructions.index("-g")
				index_h = instructions.index("-h")
				group_list = instructions[index_g+1:index_h]
				host_list = instructions[index_h+1:]
				# 删除整个组
				if instructions[index_h+1].upper() == "ALL":
					pop_list = []
					for i in group_list:
						if i in configure.keys():
							pop_list.append(i)
							configure.pop(i)
						else:
							print("There is no group named {}.".format(i))
					print("This operation will delete the group {}.".format(pop_list))
					option = input("Type [Y/y] to confirm, otherwise discard.").strip()
					if option.upper() == "Y":
						print("deleting...")
						config_handler.write(configure)
						loger.info("{} input {}, and delete the group:{}.".format(self.login_name, instructions, pop_list))
					else:
						print("give up this operation.")
						loger.debug("{} input {}, and give up to delete the group:{} in this operation.".format(self.login_name, pop_list))
				else:
					pop_list = []
					for i in group_list:
						for j in host_list:
							if j in configure.get(i, []):
								configure.get(i, []).remove(j)
								pop_list.append({i: j})
					print("This operation will delete the group:the host.")
					for i in pop_list:
						print(i)
					option = input("Type [Y/y] to confirm, otherwise discard.").strip()
					if option.upper() == "Y":
						print("deleting...")
						config_handler.write(configure)
						loger.info("{} input {}, and delete the host:{}.".format(self.login_name, instructions, pop_list))
					else:
						print("give up this operation.")
						loger.debug("{} input {}, and give up to delete the group:{} in this operation.".format(self.login_name, pop_list))

	# 批量执行命令
	def cmd(self, instructions):
		print("Execute the command in batch.")
		cmd_flag = True
		if len(instructions) < 5:
			print("Lack of arguments")
		else:
			configure = config_handler.read()
			mandatory_filed = ["-g", "-c"]
			for i in mandatory_filed:
				if i not in instructions:
					print("invalid instruction")
					cmd_flag = False
			if cmd_flag:
				index_g = instructions.index("-g")
				index_c = instructions.index("-c")
				group_list = instructions[index_g+1:index_c]
				command = instructions[index_c+1]
				for i in group_list:
					if configure.get(i):
						for j in configure[i]:
							self.amd_func(j, command)
							loger.info("{} {}:{} {}.".format(self.login_name, i, j, command))

	# 分发文件
	def sftp(self, instructions):
		sftp_flag = True
		if len(instructions) < 6:
			print("Lack of arguments")
		else:
			configure = config_handler.read()
			if "-get" in instructions:
				try:
					print("This is the func of get file from remote path.")
					index_g = instructions.index("-g")
					index_get = instructions.index("-get")
					group_list = instructions[index_g+1:index_get]
					path_list = instructions[index_get+1:]
					if len(path_list) == 2:
						for i in group_list:
							if configure.get(i):
								for j in configure[i]:
									self.sftp_get(j, path_list[0], path_list[1])
					else:
						print("Invalid instruction.")
						loger.debug("{} input {} ,and can't parse the path.".format(self.login_name, instructions))
				except ValueError as e:
					print("Invalid instruction.")
					loger.debug("{} input {},and raise error {}.".format(self.login_name, instructions, e))
			elif "-put" in instructions:
				try:
					print("This is the func of put file to remote path.")
					index_g = instructions.index("-g")
					index_get = instructions.index("-put")
					group_list = instructions[index_g+1:index_get]
					path_list = instructions[index_get+1:]
					if len(path_list) == 2:
						for i in group_list:
							if configure.get(i):
								for j in group_list[i]:
									self.sftp_get(j, path_list[0], path_list[1])
					else:
						print("Invalid instruction.")
						loger.debug("{} input {} ,and can't parse the path.".format(self.login_name, instructions))
				except ValueError as e:
					print("Invalid instruction.")
					loger.debug("{} input {},and raise error {}.".format(self.login_name, instructions, e))
			else:
				print("Invalid instruction")
				loger.debug("{} input {}.".format(self.login_name, instructions))

	# 命令解析
	def instruction_parse(self, instructions):
		instruction_list = instructions.split()
		try:
			func_str = instruction_list[0]
			if hasattr(self, func_str):
				func = getattr(self, func_str)
				func(instruction_list)
			else:
				print("Invalid instruction...")
		except IndexError as e:
			print("Invalid instruction")
			loger.debug("{} input {},{}".format(self.login_name, instructions, e))

	# 命令介绍
	def instruction_msg(self):
		msg = '''
		show -g group_name               : show the hosts under the specified group,
											all group name will show if no group been specified.
		add -g group_name -h hostname    : add the host to the group.
		delete -g group_name -h hostname : delete the host from the group.
		cmd -g group_name -c cmd         : all hosts under the group will execute the command.
		sftp -g group_name -f src dsc    : send the file to all hosts under the group.
		exit                             : exit this system.

		'''
		print(msg)

	# 登录程序
	def login(self):
		retry_count = 0
		while retry_count < 3:
			username = input("username:").strip()
			if len(username) == 0:
				continue
			# password = getpass.getpass("password:").strip()
			password = input("password:").strip()
			if len(password) == 0:
				continue
			if username in setting.USER_ACCOUNT:
				if setting.USER_ACCOUNT[username]["password"] == password:
					loger.info("{} login success.".format(username))
					print("Hi, {}, welcome to login.".format(username))
					self.login_name = username
					return True
				else:
					print("valid username or password!")
					loger.info("{} input password wrong...")
					retry_count += 1
			else:
				print("valid username or password!")
				loger.info("wrong username {}".format(username))
				retry_count += 1
		else:
			return False

	# 执行命令
	def amd_func(self, ip, cmd):
		# 创建SSH对象
		ssh = paramiko.SSHClient()
		# 允许连接不在know_hosts文件中的主机
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		# 连接服务器
		ssh.connect(hostname=ip, port=22, username="root", password="rootroot")
		# 执行命令
		stdin, stdout, stderr = ssh.exec_command(cmd)
		result1, result2 = stdout.read(), stderr.read()
		ssh.close()
		print("IP:{} return==>:".format(ip))
		if result2:
			print(result2.decode())
		else:
			print(result1.decode())

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


def run():
	q = QClient()


if __name__ == "__main__":
	a = QClient()


