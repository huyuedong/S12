#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
store all the setting
"""

import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_LEVEL = logging.INFO

LOG_TYPES = {
	"server": "ftp_server.log",
	"client": "ftp_client.log",
}

DATABASE = {
	'engine': 'file_storage',
	'name': 'accounts.db',
	'path': "{}/db".format(BASE_DIR)
}
