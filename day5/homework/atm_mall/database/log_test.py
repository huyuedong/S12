#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"


with open("log.atm", "r", encoding="gbk") as f:
	for line in f:
		print(line.strip())
