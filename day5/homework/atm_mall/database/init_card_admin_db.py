#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
初始化信用卡管理员数据库
"""

import pickle
import datetime


info = {
	"000001": {"name": "John", "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "privilege_level": 1, "created_date": datetime.date(2016, 2, 1), },
	"000002": {"name": "Tom", "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "privilege_level": 2, "created_date": datetime.date(2016, 2, 2), },
}

db_file = "card_admin.db"
with open(db_file, "wb") as fp:
	pickle.dump(info, fp)

with open(db_file, "rb") as fp:
	a = pickle.load(fp)

for k in a:
	print(k, a[k])
