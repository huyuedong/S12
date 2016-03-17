#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GROUPS_INFO = "{}{}conf{}groups.sls".format(BASE_DIR, os.sep, os.sep)

USER_ACCOUNT = {
	"alex": {
		"password": "1234", "lock_flag": "0", "limits": [],
	},
	"qimi": {
		"password": "1234", "lock_flag": "0", "limits": [],
	},
}

print(GROUPS_INFO)
