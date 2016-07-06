#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
needle 主函数
"""

from conf import configs, registered_modules
import pika
import platform
import subprocess
import json, threading
from modules import files


class CommandManagement(object):
	def __init__(self, argvs):
		self.argvs = argvs[1:]
		self.argv_handler()

	def argv_handler(self):
		if len(self.argvs) == 0:
			exit("argument: start\stop")
		if hasattr(self, self.argvs[0]):
			func = getattr(self, self.argvs[0])
			func()
		else:
			exit("invalid argument.")

	def start(self):
		client_obj = Needle()
		client_obj.listen()

	def stop(self):
		pass


class TaskHandle(object):
	"""
	任务处理类
	"""
	def __init__(self, main_obj, task_body):
		self.main_obj = main_obj  # Needle object
		self.task_body = json.loads(task_body.decode())  # Py3k need decode here

	def processing(self):
		"""
		process task
		:return:
		"""
		check_res = self.check_data_validation()
		if check_res:
			self.current_os_type, data = check_res
			self.parse_task_data(self.current_os_type, data)

	def task_callback(self, callback_queue, callback_data):
		"""
		把任务执行结果返回给服务器
		:param callback_queue:
		:param callback_data:
		:return:
		"""
		data = {
			"client_id": self.main_obj.client_id,
			"data": callback_data
		}

		# 声明queue
		self.main_obj.mq_channel.queue_declare(queue=callback_queue)
		# 设置路由
		self.main_obj.mq_channel.basic_publish(
			exchange="",
			routing_key=callback_queue,
			body=json.dumps(data)
		)
		print("[x] Sent task callback to [{}]".format(callback_queue))

	def parse_task_data(self, os_type, data):
		"""
		解析任务数据并执行
		:param os_type:
		:param data:
		:return:
		"""
		applied_list = []  # 所有已经执行了的子任务（section）放在这个列表
		applied_result = []  # 把所有应用的section的执行结果放在这里
		last_loop_section_set_len = len(applied_list)
		while True:
			for section in data:
				if section.get("callback_flag"):  # 代表已经执行过
					print("called already".center(50, "="))
				else:  # 没执行
					apply_status, result = self.apply_section(section)
					if apply_status == True:  # 执行成功
						applied_list.append(section)
						applied_result += result
			if len(applied_list) == last_loop_section_set_len:
				# 两种情况：1都执行完；2依赖关系有死锁
				print("done".center(50, "*"))
				print(len(applied_list), last_loop_section_set_len)
				print(applied_list)
				print(applied_result)
				break
			last_loop_section_set_len = len(applied_list)

		# 接下来将执行结果返回给服务器
		print("\033[42;1msend task result to task callback queue:\033[0m", self.task_body["callback_queue"])
		self.task_callback(self.task_body["callback_queue"], applied_result)

	def check_pre_requisites(self, conditions):
		"""
		检测以来条件是否成立
		:param conditions:
		:return:
		"""
		print("check pre requisites".center(50, "="))
		condition_results = []
		for condition in conditions:
			print(condition)
			cmd_res = subprocess.run(condition, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			condition_results.append(int(cmd_res.stdout.decode().strip()))
		print('\033[41;1mcmd res:\033[0m', condition_results)
		return sum(condition_results)  # 所有命令都执行成功，则返回0

	def run_cmds(self, cmd_list):
		"""
		执行命令
		:param cmd_list:
		:return:
		"""
		cmd_results = []
		for cmd in cmd_list:  # 便利执行
			print(cmd)
			cmd_res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			cmd_results.append([cmd_res.returncode, cmd_res.stderr.decode()])
			print('\033[41;1mcmd res:\033[0m', cmd_results)
			return cmd_results  # 所有命令如果执行chengg，返回0

	def apply_section(self, section_data):
		"""
		执行指定的task section
		:param section_data:
		:return:
		"""
		print("\033[32;1mapplying section\033[0m".center(50, "="))
		if section_data["required_list"] is not None:
			# 检测require条件是否满足
			if self.check_pre_requisites(section_data["required_list"]) == 0:  # 依赖满足
				if section_data.get("file_source"):  # 文件section需要单独处理
					res = self.file_handler(section_data)
				else:
					pass


