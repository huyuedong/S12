#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
redis订阅的发布者
"""

import redis

r = redis.Redis()   # 主播上班了
r.publish("fm104.5", "Hello everyone.")    # 主播跟听众打招呼
r.publish("fm104.5", "Good man is me, I am alex...")   # 主播开始hip-hop


