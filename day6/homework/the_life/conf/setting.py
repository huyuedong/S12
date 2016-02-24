#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
配置文件
"""

import os
import datetime
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)

DATABASE = {
	'engine': 'file_storage',   # support mysql,PostgreSQL in the future
	'path': "{}\db".format(BASE_PATH)
}

ACTION_TYPE = {
	"sleep": {"operator": "plus", "attr": "energy", "per_value": 50},
	"eat": {"operator": "plus", "attr": "power", "per_value": 30},
	"work": {"operator": "plus", "attr": "money", "per_value": 30},
	"learn": {"operator": "plus", "attr": "confidence", "per_value": 2},
	"consume": {"operator": "minus", "attr": "money", "per_value": 1},
}

TIME_SCALE = {
	"hour": datetime.timedelta(seconds=1),
	"day": datetime.timedelta(seconds=5),
	"year": datetime.timedelta(seconds=10),
	"ten_year": datetime.timedelta(seconds=12),
}

