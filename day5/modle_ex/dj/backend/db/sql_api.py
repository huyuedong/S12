#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

from ...config import settings


def db_auth(db):
	if db["user"] == "root" and db["password"] == "123":
		print("OK!")
		return True
	else:
		print("Error!")


def select(table, column):
	if db_auth(settings.DATABASE):
		if table == "user":
			user_info = {
				"001": ["alex", 22, "ceo"],
				"002": ["Tim", 32, "chef"],
				"003": ["john", 42, "ceo"]
			}
			return user_info
