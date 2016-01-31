#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import time
import datetime

print(time.clock())    # 输出=>3.110193534902903e-07
print(time.process_time())  # 输出=>0.031200199999999997
# 返回当前时间戳,即1970.1.1至今的秒数
print(time.time())  # 输出=>1454239454.328046

# 当前系统时间
print(time.ctime())    # 输出=>Sun Jan 31 19:24:14 2016

# 将当前时间戳转换成字符串格式的时间
print(time.ctime(time.time()))  # 输出=>Sun Jan 31 19:24:14 2016

# 将时间戳转换成struct_time格式
print(time.gmtime(time.time()))
# time.struct_time(tm_year=2016, tm_mon=1, tm_mday=31, tm_hour=11, tm_min=24, tm_sec=14, tm_wday=6, tm_yday=31, tm_isdst=0)

# 将本地时间的时间戳转换成struct_time格式
print(time.localtime(time.time()))
# time.struct_time(tm_year=2016, tm_mon=1, tm_mday=31, tm_hour=19, tm_min=24, tm_sec=14, tm_wday=6, tm_yday=31, tm_isdst=0)

# 与上面的相反,将struct_time格式转回成时间戳格式。
print(time.mktime(time.localtime()))    # 输出=>1454239454.0
