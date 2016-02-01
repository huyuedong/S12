#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
sys 模块练习
"""

import sys

# 返回命令函参数的list,第一个元素是程序本身
# sys.argv

# 退出程序,并打印括号内的内容，正常退出时exit(0)
# sys.exit(0)

# 获取Python解释器的版本信息
print(sys.version)  # 输出=>3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]

# 返回支持的最大数值
print(sys.maxsize)  # 输出=>9223372036854775807

# 返回模块的搜索路径
print(sys.path)    # 输出=>['D:\\qimi_WorkSpace\\S12\\day5', 'D:\\qimi_WorkSpace', ...]

# 返回操作系统平台名称
print(sys.platform)    # 输出=>win32

# 标准输出
sys.stdout.write('Please:')

# 标准输入
val = sys.stdin.readline()[-1]  # [-1]的作用是去掉输入时的回车

# 打印进度条...
import time
for i in range(10):
	sys.stdout.write("#")
	sys.stdout.flush()
	time.sleep(0.5)
