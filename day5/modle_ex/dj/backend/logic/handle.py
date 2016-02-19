#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

from ..db.sql_api import select


def home():
	print("welcome to home page!")
	q_data = select("user", "xxx")
	print("query res:", q_data)


def movie():
	print("welcome to movie page!")