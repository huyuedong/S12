#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
RabbitMQ实现最简单的队列通信--接收端
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()  # 创建一个频道


# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
# 为了确保队列存在在receive端也声明一下队列
channel.queue_declare(queue='hello')  # 声明一个队列


# 定义一个方法
def callback(ch, method, properties, body):
    """
    参数都为必须
    :param ch: 频道
    :param method: 方法
    :param properties: 特殊属性
    :param body: 消息体
    :return:
    """
    print(" [x] Received %r" % body)  # 打印从队列中接收到的信息

# 如果从队列里取到了数据就会执行callback函数
channel.basic_consume(callback,  # 收到消息后执行的操作
                      queue='hello',
                      no_ack=True)  # 不需要应答

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
