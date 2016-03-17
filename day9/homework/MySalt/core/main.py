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
import multiprocessing
import paramiko
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
			'300': "300...",
			'301': "301...",
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
	def exit(self, instructions):
		print("Bye~")
		loger.info("{} logout.".format(self.login_name))
		self.__exit_flag = True

	# 查看主机分组
	def show(self, instructions):
		print("show group of host...")
		# 读取配置
		configure = config_handler.read()
		# 只有一个show的时候默认打印所有的组名
		if len(instructions) == 1:
			print("{:*^50}".format("groups"))
			for k in configure:
				print(k)
			print("-" * 50)
		elif "-g" in instructions:
			# 获取用户输入的组名
			group_list = instructions[instructions.index("-g")+1:]
			# 如果有这个组名，就遍历打印出这个组下的所有主机记录
			try:
				# 遍历用户输入的组名列表
				for i in group_list:
					# 如果配置文件中有这个组名
					if i in configure:
						print("{:*^50}".format(i))
						# 遍历打印该组的主机记录
						for j in configure[i]:
							print(j)
							loger.info("{} checkout the host of the group:{}.".format(self.login_name, i))
						print("-" * 50)
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

	# 命令解析
	def instruction_parse(self, instructions):
		# 判断命令是否是有效命令
		if instructions.strip().startswith("mysalt"):
			# 按空格分割得到列表
			instruction_list = instructions.split()
			# 过滤掉<' " ,>
			arg_list = list(map(lambda t: re.sub(r'[,"\']', "", t), instruction_list))
			go_flag = False     # 定义一个继续解析的标志
			count_point_item = 0    # 确保只有一项是包含.的
			global module_func  # 指令列表中包含<包名.方法>的那一项
			for i in arg_list:
				if i.count(".") > 0:
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
						func = getattr(self, func_name)
						func(arg)
					else:
						print("Invalid instruction...")
						self.instruction_msg()
				except ImportError as e:
					print("Can't find that module.")
					loger.info("input:{}, error:{}".format(instructions, e))
			else:
				print("Invalid instruction.")
				self.instruction_msg()
		else:
			print("Invalid instruction.")
			self.instruction_msg()

	# 命令介绍
	def instruction_msg(self):
		print("The help info:")
		msg = '''
		salt "*" cmd.run "instructions"                          : run the instructions on all hosts
		salt -g "group_name" cmd.run "instructions"              : run instruction on hosts under the group
		salt "*" file.put "filename"                             : put the specified file to all hosts
		salt "*" file.get "filename"                             : get the specified file from all hosts
		exit                                                     : exit this system.

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


