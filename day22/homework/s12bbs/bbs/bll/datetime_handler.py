#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
处理时间
用于前端展示的时间戳
"""

from datetime import datetime, timezone


def readable_date(pub_date):
    current_date = datetime.now(timezone.utc)  # 获得UTC时间,方便比较
    diff_date = current_date - pub_date
    total_seconds = diff_date.total_seconds()
    if total_seconds >= 86400:
        time_interval = str(int(divmod(total_seconds, 86400)[0])) + "天前"
    elif total_seconds >= 3600:
        time_interval = str(int(divmod(total_seconds, 3600)[0])) + "小时前"
    elif total_seconds >= 60:
        time_interval = str(int(divmod(total_seconds, 60)[0])) + "分钟前"
    else:
        time_interval = "刚刚"
    return time_interval
