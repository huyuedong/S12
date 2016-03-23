#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
RabbitMQ实现简单的队列通信--发送端
"""
import pika

# 建立链接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

# 实例化链接
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# RabbitMQ的消息并不能直接发送到队列，它需要经过交换机的分发。
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
