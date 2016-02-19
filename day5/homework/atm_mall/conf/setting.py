#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
文件配置
"""
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCOUNT_DB = "{}\\database\\card_account.db".format(BASE_PATH)
ADMIN_DB = "{}\\database\\card_admin.db".format(BASE_PATH)
RECORD_DB = "{}\\database\\record.db".format(BASE_PATH)
MALL_ACCOUNT_DB = "{}\\database\\account.db".format(BASE_PATH)
LOG_ATM = "{}\\database\\log.atm".format(BASE_PATH)
