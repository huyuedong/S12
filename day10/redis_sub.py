#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
订阅的接收者
"""

import redis

r = redis.Redis()
sub = r.pubsub()    # 打开收音机
sub.subscribe("fm104.5")    # 拧到fm104.5
sub.parse_response()    # 准备收听

while True:
	msg = sub.parse_response()      # 开始收听
	print(msg)  # 收听到大保健信息

