#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
The client settings
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

Params = {
	# TODO change to your server address
	"server": "0.0.0.0",
	"port": 8000,
	"request_timeout": 30,
	"urls": {
		"asset_report_with_no_id": "/asset/report/asset_with_no_asset_id/",  # 第一次资产汇报时的地址
		"asset_report": "/asset/report/",  # 资产汇报的地址
	},
	"asset_id": "{}/var/.asset_id".format(BASE_DIR),
	"log_file": "{}/logs/winterfell_log".format(BASE_DIR),
	# TODO change to your auth
	"auth": {
		"user": "master@liwenzhou.com",
		"token": "1234",
	},
}
