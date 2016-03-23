#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
消息消费者
关键字发送
exchange_type=direct
direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
之前事例，发送消息时明确指定某个队列并向其中发送消息，RabbitMQ还支持根据关键字发送，
即：队列绑定关键字，发送者将数据根据关键字发送到消息exchange，exchange根据 关键字 判定应该将数据发送至指定队列。
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',  # 明明交换机
                         type='direct')  # 设置交换机类型

# 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


# 该消费者接收info和debug类的消息。
channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key="info",
                   )
channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key="debug",
                   )

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] {}:{}".format(method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
