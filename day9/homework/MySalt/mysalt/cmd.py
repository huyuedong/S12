#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
the cmd execution module
mysalt "operate object" module.func "instruction"
arg = ["operate object", module.func, "instruction"]
"""
import paramiko


def run(arg):
	pass


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

