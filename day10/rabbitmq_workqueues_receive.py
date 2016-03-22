#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
工作队列：默认把消息发送给每一个接收者
消息消费者
先启动消息生产者，然后再分别启动3个消息消费者，通过生产者多发送几条消息，你会发现，这几条消息会被依次分配到各个消费者。
"""

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()


def callback(ch, method, properties, body):
	print("[x] Received {}".format(body))

	time.sleep(body.count(b'.'))
	print("[x] Done!")
	ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(callback, queue="task_queue",)
print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
