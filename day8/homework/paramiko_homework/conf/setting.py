#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = "{}\conf\config.json".format(BASE_DIR)

USER_ACCOUNT = {
	"alex": {
		"password": "1234", "lock_flag": "0", "limits": [],
	},
	"qimi": {
		"password": "1234", "lock_flag": "0", "limits": [],
	},
}
