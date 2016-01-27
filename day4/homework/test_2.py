#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import re
s = "9-3.3333333333333335+173134.50000000003+405.7142857142857"
result = re.search(r'[\-\+]?\d*\.?\d+[\+\-]\d+\.?\d*', s)
if result:
	print(result.group())

