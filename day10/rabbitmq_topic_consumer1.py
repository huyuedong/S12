#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

"""
更细致的消息过滤
# 表示可以匹配 0 个 或 多个 单词
* 表示只能匹配 一个 单词

'#':匹配所有log
'*.critical':匹配到所有程序的critical级别的log
'tomcat.*'：匹配到所有tomcat的log
'tomcat.*' '*.critical':匹配到tomcat的所有级别的log以及所有程序的critical级别的log
'tomcat.critical' 'A critical tomcat error'：匹配到tomcat.critical和A critical tomcat error的log
"""

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: {} [binding_key]...\n".format(sys.argv[0]))
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] {}:{}".format(method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
