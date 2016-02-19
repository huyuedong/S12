#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
记录消费记录
"""

import os
import time
import json
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conf import setting


# 记录消费记录
def transaction_record(card_id, description, rmb_amount,):
	file_name = setting.RECORD_dB
	try:
		rmb_amount = float(rmb_amount)
		record_id = str(float(time.time()))    # 生成一个流水号
		info = {record_id: {}}
		info[record_id]["card_id"] = card_id
		info[record_id]["tran_date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
		info[record_id]["description"] = description
		info[record_id]["rmb_amount"] = rmb_amount
		with open(file_name, "a") as fp:
			s = json.dumps(info)
			fp.write("{}\n".format(s))
	except TypeError:
		return None

# transaction_record(1, 2, 3)

# with open("D:\\GitHub\\S12\day5\\homework\\atm_mall\database\\record.db", "r") as f:
# 	for line in f:
# 		d_temp = json.loads(line)
# 		for k in d_temp:
# 			print(k, d_temp[k])
