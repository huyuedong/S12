#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import time
import datetime

# time模块

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

# sleep
# time.sleep(4)

# 将struct_time格式转成指定的字符串格式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))  # 输出=>2016-02-01 13:53:22

# 将字符串格式转成struct_time格式
print(time.strptime("2016-02-01", "%Y-%m-%d"))
# time.struct_time(tm_year=2016, tm_mon=2, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=32, tm_isdst=-1)

# datetime 模块

print(datetime.date.today())    # 输出=>2016-02-01

print(datetime.date.fromtimestamp(time.time() - 86640))    # 输出=>2016-01-31

current_time = datetime.datetime.now()
print(current_time)    # 输出=>2016-02-01 14:01:02.428880
# 返回struct_time格式的时间
print(current_time.timetuple())
# time.struct_time(tm_year=2016, tm_mon=2, tm_mday=1, tm_hour=14, tm_min=1, tm_sec=41, tm_wday=0, tm_yday=32, tm_isdst=-1)

# 指定替换
# datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])
print(current_time.replace(2008, 8, 8))    # 输出=>2008-08-08 14:03:53.901093

# 将字符串转换成日期格式
str_to_date = datetime.datetime.strptime("2016-02-01", "%Y-%m-%d")
print(str_to_date)  # 输出=>2016-02-01 00:00:00

# 比现在+10d
new_date = datetime.datetime.now() + datetime.timedelta(days=10)
print(new_date)    # 输出=>2016-02-11 14:46:49.158138

# 比现在-10d
new_date = datetime.datetime.now() - datetime.timedelta(days=10)
print(new_date)    # 输出=>2016-01-22 14:53:03.712109

# 比现在+10h
new_date = datetime.datetime.now() + datetime.timedelta(hours=10)
print(new_date)    # 输出=>2016-02-02 00:53:03.712109

# 比现在+120s
new_date = datetime.datetime.now() + datetime.timedelta(seconds=120)
print(new_date)    # 输出=>2016-02-01 14:55:03.712109




