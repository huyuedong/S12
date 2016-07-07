#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
任务处理
"""

import pika
import json


class TaskHandle(object):
	"""
	generate task
	"""
	def __init__(self, db_model, task_data, settings, module_obj):
		self.db_model = db_model
		self.task_data = task_data
		self.settings = settings
		self.module_obj = module_obj  # 调用者
		self.make_connection()

	def apply_new_task(self):
		"""
		在数据库中创建一条任务，并返回ID值
		:return:
		"""
		new_task_obj = self.db_model.Task()
		new_task_obj.save()
		self.task_id = new_task_obj.id
		return True

	def dispatch_task(self):
		"""
		格式化任务，准备发送
		:return:
		"""
		if self.apply_new_task():
			print("Send task to:", self.module_obj.host_list)
			self.callback_queue_name = "TASK_CALLBACK_{}".format(self.task_id)
			data = {
				"data": self.task_data,
				"id": self.task_id,
				"callback_queue": self.callback_queue_name,
				"token": None
			}

			print("task data".center(50, "="))
			for os_type, os_config_data in self.task_data.items():
				print("==>os:", os_type)
				for mod_data in os_config_data:
					print("mod data".center(16, "="))
					print(mod_data)
			print("end task data".center(50, "="))

			for host in self.module_obj.host_list:
				self.publish(data, host)

			# 开始等待任务结果
			self.wait_callback()

	def make_connection(self):
		print("settings mq", self.settings.MQ_CONN)
		self.mq_conn = pika.BlockingConnection(pika.ConnectionParameters(
			self.settings.MQ_CONN["host"],
			port=self.settings.MQ_CONN["port"]
		))
		self.mq_channel = self.mq_conn.channel()

	def publish(self, task_data, host):
		print("\033[41;1m ---- going to publish msg ----\033[0m;\n")

		# 声明queue
		queue_name = "TASK_Q_{}".format(host.id)
		self.mq_channel.queue_declare(queue=queue_name)

		print(json.dumps(task_data).encode())

		self.mq_channel.basic_publish(
			exchange="",
			routing_key=queue_name,
			body=json.dumps(task_data)
		)

		print("[x] Sent task to queue [{}] 'Hello World!'.".format(queue_name))

	def close_connection(self):
		self.mq_conn.close()

	def task_callback(self, ch, method, properties, body):
		print(body)

	def wait_callback(self):
		"""
		回执
		:return:
		"""
		self.mq_channel.queue_declare(queue=self.callback_queue_name)
		self.mq_channel.basic_consume(
			self.task_callback,
			queue=self.callback_queue_name,
			no_ack=True
		)

		print("\033[42;1m[{}] Waiting for callback. To exit press CTRL+C\033[0m".format(self.callback_queue_name))
		self.mq_channel.start_consuming()
