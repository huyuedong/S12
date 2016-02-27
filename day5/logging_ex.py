#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
logging模块的练习
"""
import logging

# logfile = "example.log"
# logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#
# logging.warning("user [alex] attempted wrong passwd more than 3 times")
# logging.critical("server is down!")
# logging.debug('This message should be go to the log file...')
# logging.warning("Server is down!")

# 同时输出到文件和屏幕
logger = logging.getLogger("LOG-TEST")  # 创建一个logger
logger.setLevel(logging.DEBUG)  # 设定logging 级别，logging的级别以最高的为主

ch = logging.StreamHandler()    # 创建一个输出到屏幕的handler
ch.setLevel(logging.INFO)   # 设置logging级别

fh = logging.FileHandler("test.log")  # 创建一个文件handler
fh.setLevel(logging.WARNING)    # 设置logging级别

# 创建格式
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')

