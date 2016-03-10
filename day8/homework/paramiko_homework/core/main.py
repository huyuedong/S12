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
import getpass
import multiprocessing
import paramiko
import logging
import Mylogging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import configure_handler
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
		configure = configure_handler.read()
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
				for k in configure.get(group_name, None):
					print("hostname:{}".format(k))
					print("ip:{} port:{}".format(configure[group_name].get("ip"), configure[group_name].get("port")))
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
		# 参数小于5，就提示参数不足
		if len(instructions) < 5:
			print("Lack of arguments")
		else:
			mandatory_filed = ["-g", "-h"]
			for i in mandatory_filed:
				if i not in instructions:
					print("invalid instruction")

		configure = configure_handler.read()


	# 删除主机
	def delete(self, instructions):
		pass

	# 批量执行命令
	def cmd(self, instructions):
		pass

	# 分发文件
	def sftp(self, instructions):
		pass

	# 命令解析
	def instruction_parse(self, instructions):
		instruction_list = instructions.split()
		func_str = instruction_list[0]
		if hasattr(self, func_str):
			func = getattr(self, func_str)
			func(instruction_list)
		else:
			print("Invalid cmd...")

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


if __name__ == "__main__":
	a = QClient()


