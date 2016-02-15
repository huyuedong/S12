#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
测试db
"""

import pickle
import datetime


info = {
	"88888881":
		{"name": "alex", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 20000,
			"cash_limit": 10000, "current_limit": 20000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
	"88888882":
		{"name": "john", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 10000,
			"cash_limit": 5000, "current_limit": 10000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
}

db_file = "card_account.db"
with open(db_file, "wb") as fp:
	pickle.dump(info, fp)

with open(db_file, "rb") as fp:
	a = pickle.load(fp)

for k in a:
	print(k, a[k])
