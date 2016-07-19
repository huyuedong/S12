#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
API Token
"""
import hashlib, time


def get_token(username, token_id):
	timestamp = int(time.time())
	md5_format_str = "{}\n{}\n".format(username, timestamp, token_id)  # 拼接信息
	obj = hashlib.md5()
	obj.update(md5_format_str)  # 生成MD5值
	print("token format:{}".format(md5_format_str))
	print("token:[{}]".format(obj.hexdigest()))  # 16进制MD5值
	return obj.hexdigest()[10:17], timestamp  # 返回16进制MD5值的10-16位和时间戳


if __name__ == "__main__":
	print(get_token("qimi", "1234"))
