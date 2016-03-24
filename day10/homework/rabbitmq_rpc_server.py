#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
RPC server端：消息的订阅者
master端向server端发送一个数，并接收server端返回斐波那契数列的和
"""

import pika
import subprocess
import os

credentials = pika.PlainCredentials('test', 'test')  # 建立认证
connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.18.18.18",
                                                               port=5672,
                                                               credentials=credentials,
                                                               ))

channel = connection.channel()

channel.exchange_declare(exchange="cmd", exchange_type="fanout",)

channel.queue_bind(exchange="cmd", queue="rpc_queue")  # 绑定交换机和队列


# 定义一个运行命令的方法
def run(cmd):
	# result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	# return result.stdout.read()
	# print("Running {} ...".format(cmd))
	# return "Result==>{}".format(cmd)
	result = os.system(cmd)
	return result


# 定义一个回调函数,
def on_request(ch, method, props, body):
	body = str(body)
	print(" [.] Get the instruction:{}".format(body))  # 打印提示信息
	response = run(body)  # 计算得到结果
	# 发送结果信息
	ch.basic_publish(
			exchange="",
			routing_key=props.reply_to,  # 关键字为返回消息的队列
			properties=pika.BasicProperties(correlation_id=props.correlation_id),
			body=str(response),  # 消息体
			)
	ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送应答


channel.basic_qos(prefetch_count=1)  # 公平分发
channel.basic_consume(on_request, queue="rpc_queue")  # 将回调函数传入basic_consume

print(" [x] waiting RPC requests.")
channel.start_consuming()
