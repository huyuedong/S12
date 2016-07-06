#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
needle的配置信息
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SALT_MASTER = "localhost"

FILE_SERVER = {
	"http": "{}:8000".format(SALT_MASTER.strip()),
	"salt": SALT_MASTER
}

FILE_SERVER_BASE_PATH = "/salt/file_center"

FILE_STORE_PATH = "{}/var/downloads/".format(BASE_DIR)


# tmp config
NEEDLE_CLIENT_ID = 1


# rabbitMQ连接信息
MQ_CONN = {
	"host": "localhost",
	"port": 4000,
	"password": ""
}
