#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
logging模块的练习
"""
import logging
import time
import datetime
import os
logfile = "D:\GitHub\S12\day5\example.log"

logging.warning("user [alex] attempted wrong passwd more than 3 times")
logging.critical("server is down!")

logging.basicConfig(filename=logfile, level=logging.INFO)
logging.debug('This message should be go to the log file...')
logging.info("{} {}".format(datetime.datetime.today(), time.ctime(time.time())))
logging.warning("Server is down!")
