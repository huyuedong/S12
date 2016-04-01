#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "liwenzhou"
# Email: master@liwenzhou.com

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_CONN = "mysql+pymysql://root:1234@localhost:3306/StupidJumpServer"

CONFIG_BASE_PATH = "{}{}home".format(BASE_DIR, os.sep)

DATABASE = {
	"db_type": "mysql",
	"engine": "pymysql",
	"username": "root",
	"password": "1234",
	"host": "localhost",
	"port": 3306,
	"db_name": "stupidjumpserver",
}
