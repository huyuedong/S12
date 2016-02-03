#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import pickle

with open("trade_db.dat.dat", "rb") as f:
	d1 = pickle.load(f)
	print(d1)


