#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

import os
import sys


if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Stark.setting")
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	sys.path.append(BASE_DIR)

	from Arya.backends.utils import ArgvManagement
	obj = ArgvManagement(sys.argv)
