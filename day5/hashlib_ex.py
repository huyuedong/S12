#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
hashlib模块的练习
"""

import hashlib
import hmac

# # MD5
# h1 = hashlib.md5()
# h1.update("admin".encode("utf-8"))
# print(h1.digest())
# print(h1.hexdigest())
#
# # sha1
# h2 = hashlib.sha1()
# h2.update("admin".encode("utf-8"))
# print(h2.digest())
# print(h2.hexdigest())
#
# # sha256
# h3 = hashlib.sha256()
# h3.update("admin".encode("utf-8"))
# print(h3.digest())
# print(h3.hexdigest())
#
# # sha384
# h4 = hashlib.sha384()
# h4.update("admin".encode("utf-8"))
# print(h4.digest())
# print(h4.hexdigest())
#
# # sha512
# h5 = hashlib.sha512()
# h5.update("admin".encode("utf-8"))
# print(h5.digest())
# print(h5.hexdigest())
#
# # 在加密算法中添加自定义key
# h6 = hashlib.md5("466485959".encode("utf-8"))
# h6.update("admin".encode("utf-8"))
# print(h6.digest())
# print(h1.digest())
# print(h6.hexdigest())
# print(h1.hexdigest())
#
# # 更高级的hmac模块，对自建key处理之后再加密
# h7 = hmac.new("466485959".encode("utf-8"))
# h7.update("admin".encode("utf-8"))
# print(h7.digest())
# print(h7.hexdigest())


# 预设一个加密算法
def md5_encry(str):
	try:
		# 将传入的参数按utf-8编码
		m = str.encode("utf-8")
		# 创建添加自定义key的md5对象
		h = hashlib.md5("alex".encode("utf-8"))
		# 生成加密串
		h.update(m)
		# 返回十六进制的加密串
		return h.hexdigest()
	except TypeError:
		return None
i_pw = md5_encry("466485959")

pw = input("pw:")

if md5_encry(pw) == i_pw:
	print("yeah!Welcome you!")
else:
	print("sorry!")
