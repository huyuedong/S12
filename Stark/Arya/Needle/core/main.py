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
					res = self.file_handle(section_data)
				else:
					res = self.run_cmds(section_data["raw_cmds"])
				section_data["called_flag"] = True
				return [True, res]
			else:
				print("\033[33;1m依赖不满足\033[0m")
				return [False, None]
		else:  # 没有依赖要求，直接执行
			if section_data.get("file_source") is True:  # 文件section需单独处理
				res = self.file_handle(section_data)
			else:
				res = self.run_cmds(section_data["raw_cmds"])
			section_data["called_flag"] = True
			return [True, res]

	def file_handle(self, section_data):
		"""
		对文件进行操作
		:param section_data:
		:return:
		"""
		file_module_obj = files.FileModule(self)
		file_module_obj.process(section_data)
		return []

	def check_data_validation(self):
		"""
		确保服务器发来的任务在本客户端上可以执行
		:return:
		"""
		print("parse task".center(50, "="))
		os_version = platform.version().lower()
		for os_type, data in self.task_body["data"].items():
			print(os_version, os_type)
			if os_type not in os_version:  # should be in ,only for test
				print(os_type, data)
				return os_type, data
		else:
			print("\033[31;1msalt is not supported on this OS \033[0m", os_version)


class Needle(object):

	def __init__(self):
		self.configs = configs
		self.make_connection()
		self.client_id = self.get_needle_id()
		self.task_queue_name = "TASK_Q_{}".format(self.client_id)

	def get_needle_id(self):
		"""
		去服务器端取自己的id
		:return:
		"""
		return configs.NEEDLE_CLIENT_ID

	def listen(self):
		"""
		开始监听服务器的call
		:return:
		"""
		self.msg_consume()

	def make_connection(self):
		"""
		创建连接
		:return:
		"""
		self.mq_conn = pika.BlockingConnection(pika.ConnectionParameters(
			configs.MQ_CONN["host"],
		))
		self.mq_channel = self.mq_conn.channel()

	def publish(self, data):
		print("\033[41;1m====going to publish msg====\033[0m", data)
		# 声明queue
		self.mq_channel.queue_declare(queue="hello")
		#
		self.mq_channel.basic_publish(
			exchange="",
			routing_key="hello",
			body="Hello World!"
		)
		print("[x] Sent 'Hello world!'")
		self.mq_conn.close()

	def msg_callback(self, ch, method, properties, body):
		print("[x] Received a task msg.")
		thread = threading.Thread(
			target=self.start_thread,
			args=(body,)
		)
		thread.start()

	def start_thread(self, task_body):
		print("\033[31;1m Start a thread to process task\033[0m")
		task = TaskHandle(self, task_body)
		task.processing()

	def msg_consume(self):
		self.mq_channel.queue_declare(queue=self.task_queue_name)
		self.mq_channel.basic_consume(
			self.msg_callback,
			queue=self.task_queue_name,
			no_ack=True
		)

		print("[{}] Waiting for messages. To exit press CTRL+C".format(self.task_queue_name))
		self.mq_channel.start_consuming()
