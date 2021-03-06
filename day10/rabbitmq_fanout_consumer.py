#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
订阅者
exchange_type=fanout:
fanout: 所有bind到此exchange的queue都可以接收消息
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="apple",
                         exchange_type="fanout",
                         )
result = channel.queue_declare(exclusive=True)  # 设置频道排外
queue_name = result.method.queue
channel.queue_bind(exchange="apple", queue=queue_name)

print("[*] Waiting for message.To exit press CTRL+C.")


def callback(ch, method, properties, body):
    print("[x] {}".format(body))

channel.basic_consume(callback, queue=queue_name, no_ack=True)

channel.start_consuming()


