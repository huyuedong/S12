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
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger(__name__)

# credentials = pika.PlainCredentials('test', 'test')  # 建立认证
# connection = pika.BlockingConnection(pika.ConnectionParameters(host="", port=5672, credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))

channel = connection.channel()

channel.exchange_declare(exchange="cmd", exchange_type="fanout",)

channel.queue_bind(exchange="cmd", queue="rpc_queue")  # 绑定交换机和队列


# 定义一个运行命令的方法
def run(cmd):
	result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	logger.info("Running {} ...".format(cmd))
	# result = os.system(cmd)
	logger.info("Result:{}.".format(result.stdout.read()))
	return result.stdout.read()


# 定义一个回调函数,
def on_request(ch, method, props, body):
	body = str(body)
	logger.info(" [.] Get the instruction:{}".format(body))  # 打印提示信息
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

logger.info(" [x] waiting RPC requests.")
channel.start_consuming()
