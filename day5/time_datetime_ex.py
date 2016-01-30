#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import time
import datetime

print(time.clock())
print(time.process_time())
# 返回当前时间戳
print(time.time())

# 当前系统时间
print(time.ctime())

# 将当前时间戳转换成字符串格式的时间
print(time.ctime(time.time()))

# 将时间戳转换成struct_time格式
print(time.gmtime(time.time()))

# 将本地时间的时间戳转换成struct_time格式
print(time.localtime(time.time()))

# 与上面的
