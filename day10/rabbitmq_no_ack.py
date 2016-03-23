#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
ack应答
1、acknowledgment 消息不丢失

no-ack ＝ False（默认），如果消息的消费者遇到情况(its channel is closed, connection is closed, or TCP connection is lost)挂掉了，
那么，RabbitMQ会重新将该任务添加到队列中。
消息的生产者端代码不需要改变。
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):
	print("[x] Received {}.".format(body))
	# 10秒内结束程序，模拟消费者掉线；再次启动消费者时还会收到该条信息
	import time
	time.sleep(10)
	print("OK")
	ch.basic_ack(delivery_tag=method.delivery_tag)  # 消息已被处理，返回应答

channel.basic_consume(callback, queue="hello", no_ack=False)

print("[*] Waiting for message.To exit press CTRL+C.")
channel.start_consuming()

