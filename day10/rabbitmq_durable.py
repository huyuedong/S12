#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
消息队列持久化，防止消息的生产者宕机等引起的消息丢失
 -声明队列时要持久化
 -发送消息时也要持久化
 两个都要声明
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.211.55.4'))
channel = connection.channel()

# make message persistent
channel.queue_declare(queue='hello', durable=True)  # 在声明队列时要增加durable的声明

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # 在发送消息是也要设置消息持久化
                      ))
print(" [x] Sent 'Hello World!'")
connection.close()
