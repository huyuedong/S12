#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com


"""
工作队列：默认把消息发送给每一个接收者
消息生产者
先启动消息生产者，然后再分别启动3个消息消费者，通过生产者多发送几条消息，你会发现，这几条消息会被依次分配到各个消费者。
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))


channel = connection.channel()

# 声明队列
channel.queue_declare(queue="task_queue")

# RabbitMQ的消息都不能直接发送到队列中，必须要经过一个交换机。
import sys

message = "".join(sys.argv[1:]) or "Hello world!"  # 定义消息内容
channel.basic_publish(
	exchange="",  # 交换机
	routing_key="task_queue",
	body=message,  # 发送的消息
	properties=pika.BasicProperties(
		delivery_mode=2,  # 设置消息持久化
	)
)


print("[x] Sent {}".format(message))
connection.close()
