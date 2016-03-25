#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
RPC minion端：消息的订阅者
master端向minion端发送一个命令，并接收minion端返回的命令执行结果
"""

import pika
import subprocess
import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

logger = logging.getLogger(__name__)


# 定义一个运行命令的方法
def excute(cmd):
	result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	logger.info("Running {} ...".format(cmd))
	# result = os.system(cmd)
	logger.info("Result:{}.".format(result.stdout.read()))
	return result.stdout.read()


# 定义一个回调函数,
def on_request(ch, method, props, body):
	body = str(body)
	logger.info(" [.] Get the instruction:{}".format(body))  # 打印提示信息
	result = excute(body)  # 得到执行结果
	p = subprocess.Popen("hostname", shell=True, stdout=subprocess.PIPE)
	hostname = p.stdout.read()  # 得到本机主机名
	response = """
	hostname:{}
	execute result:
	{}
	""".format(hostname, str(result))
	# 发送结果信息
	ch.basic_publish(
			exchange="",
			routing_key=props.reply_to,  # 关键字为返回消息的队列
			properties=pika.BasicProperties(correlation_id=props.correlation_id),
			body=str(response),  # 消息体
			)
	ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送应答


def run():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))  # 链接RabbitMQ

	channel = connection.channel()  # 声明频道
	channel.queue_declare(queue="rpc_queue", durable=True)  # 声明一个rpc的队列，用户接收命令

	channel.exchange_declare(exchange="cmd", exchange_type="fanout",)

	channel.queue_bind(exchange="cmd", queue="rpc_queue")  # 绑定交换机和队列
	channel.basic_qos(prefetch_count=1)  # 公平分发
	channel.basic_consume(on_request, queue="rpc_queue")  # 将回调函数传入basic_consume

	logger.info(" [x] waiting RPC requests.")
	channel.start_consuming()

if __name__ == "__main__":
	connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port=5672))  # 链接RabbitMQ

	channel = connection.channel()  # 声明频道
	channel.queue_declare(queue="rpc_queue", durable=True)
	channel.exchange_declare(exchange="cmd", exchange_type="fanout",)  #

	channel.queue_bind(exchange="cmd", queue="rpc_queue")  # 绑定交换机和队列
	channel.basic_qos(prefetch_count=1)  # 公平分发
	channel.basic_consume(on_request, queue="rpc_queue")  # 将回调函数传入basic_consume

	logger.info(" [x] waiting RPC requests.")
	channel.start_consuming()
