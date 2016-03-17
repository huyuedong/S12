#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
可以对机器进行分组
可以对指定的一组或多组机器执行批量命令，分发文件(发送\接收)
使用SaltStack的模式,实现上节课的远程管理主机
MySalt "operate object" module.func "instruction"
配置文件使用yaml格式
纪录操作日志
version: v0.1
"""

import os
import sys
import re
import getpass
import yaml
import logging
import importlib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting

loger = logging.getLogger(__name__)


class QClient(object):

	# 错误代码
	def __init__(self):
		self.response_code = {
			'200': "Invalid username or password!",
			'201': "Too many retry!",
			'202': "202...",
			'300': "Invalid instruction.",
			'301': "Can't find that module.",
			'302': "302...",
		}
		self.login_name = None
		self.__exit_flag = False
		if self.login():
			self.menu()

	# 主菜单
	def menu(self):
		print("This is a batch host management tool.")
		while not self.__exit_flag:
			user_input = input("[{}]==>".format(self.login_name)).strip()
			self.instruction_parse(user_input)

	# 退出
	def exit(self):
		print("Bye~")
		loger.info("{} logout.".format(self.login_name))
		self.__exit_flag = True

	# 命令解析
	def instruction_parse(self, instructions):
		loger.debug("{} input {}.".format(self.login_name, instructions))
		# 判断命令是否是有效命令
		if instructions.strip().startswith("mysalt"):
			# 按空格分割得到列表
			instruction_list = instructions.split()
			# 过滤掉<' " ,>
			arg_list = list(map(lambda t: re.sub(r'[,\"\']', "", t), instruction_list))
			go_flag = False     # 定义一个继续解析的标志
			count_point_item = 0    # 确保只有一项是包含.的
			global module_func  # 指令列表中包含<包名.方法>的那一项
			p = re.compile(r'[a-zA-Z_]+\.[a-zA-Z_]+')
			for i in arg_list:
				if p.match(i):
					go_flag = True
					module_func = i
					count_point_item += 1
			# 当且仅当有一项是包含.的时候，继续解析
			if go_flag and count_point_item == 1:
				cmd_list = arg_list[arg_list.index(module_func)+1:]     # 得到出指令的列表
				obj_list = arg_list[arg_list.index("mysalt")+1:arg_list.index(module_func)]     # 得到操作对象的列表
				arg = (obj_list, cmd_list)  # 将操作对象列表和指令列表放到元祖中
				module_name = module_func.split(".")[0]     # 获取到包名
				func_name = module_func.split(".")[1]   # 获取到方法名
				try:
					# 导入命令中需要的包
					module = importlib.import_module("mysalt.mysalt_{}".format(module_name))
					# 判断是否有命令中的方法
					if hasattr(module, func_name):
						print("=" * 50)
						func = getattr(module, func_name)
						print("-" * 50)
						func(arg)
					else:
						print(self.response_code["300"])
						self.instruction_msg()
				except ImportError as e:
					print(self.response_code["301"])
					loger.info("input:{}, error:{}".format(instructions, e))
			else:
				print(self.response_code["300"])
				self.instruction_msg()
		elif instructions.strip().upper() == "EXIT":
			self.exit()
		elif instructions.strip() == "?" or instructions.strip().upper() == "HELP":
			self.instruction_msg()
		else:
			print(self.response_code["300"])
			self.instruction_msg()

	# 命令介绍
	def instruction_msg(self):
		print("The help info:")
		msg = '''
		mysalt "*" cmd.run "instructions"                          : run the instructions on all hosts
		mysalt -g "group_name" cmd.run "instructions"              : run instruction on hosts under the group
		mysalt -h "host_name" cmd.run "instructions"               : run instruction on the specified hosts
		mysalt "*" file.put "filename"                             : put the specified file to all hosts
		mysalt "*" file.get "filename"                             : get the specified file from all hosts
		exit                                                       : exit this system.

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
					print(self.response_code["200"])
					loger.info("{} input password wrong...")
					retry_count += 1
			else:
				print(self.response_code["200"])
				loger.info("wrong username {}".format(username))
				retry_count += 1
		else:
			print(self.response_code["201"])
			return False


def run():
	q = QClient()


if __name__ == "__main__":
	a = QClient()


