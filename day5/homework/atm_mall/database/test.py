#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
import pickle
import datetime

info = {
	"alex":
		{"name": "alex", "age": 18, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "email": "123456@163.com", "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
	"john":
		{"name": "john", "age": 18, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "email": "654321@163.com", "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
}
db_file = "account.db"
with open(db_file, "wb") as f:
	pickle.dump(info, f)


with open(db_file, "rb") as fp:
	a = pickle.load(fp)
for k in a:
	print(k, a[k])


