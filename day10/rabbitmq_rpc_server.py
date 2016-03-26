#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
RPC server端
client端向server端发送一个数，并接收server端返回斐波那契数列的和
"""

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue="rpc_queue")


def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


# 定义一个回调函数
def on_request(ch, method, props, body):
	n = int(body)  # 把收到的消息转成int类型
	print("[.] fib({})".format(n))  # 打印提示信息
	response = fib(n)  # 计算得到结果
	# 返回结果信息
	ch.basic_publish(
			exchange="",  # 交换机为空
			routing_key=props.reply_to,  # 关键字为reply_to
			properties=pika.BasicProperties(correlation_id=props.correlation_id),
			body=str(response),
			)
	ch.basic_ack(delivery_tag=method.delivery_tag)  # 发送应答


channel.basic_qos(prefetch_count=1)  # 公平分发
channel.basic_consume(on_request, queue="rpc_queue")

print("[x] waiting RPC requests.")
channel.start_consuming()
