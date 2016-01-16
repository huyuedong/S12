#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
自定义的函数
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# def send_mail_to_wu(user):
# 	ret = 1
# 	try:
# 		msg = MIMEText('邮件内容', 'plain', 'utf-8')
# 		msg['From'] = formataddr(["武沛齐",'wptawy@126.com'])
# 		msg['To'] = formataddr(["走人",'466485959@qq.com'])
# 		msg['Subject'] = "主题"
#
# 		server = smtplib.SMTP("smtp.126.com", 25)
# 		server.login("wptawy@126.com", "WW.3945.59")
# 		server.sendmail('wptawy@126.com', [user, ], msg.as_string())
# 		server.quit()
# 	except Exception:
# 		ret = 2
# 	return ret
#
# ss1 = send_mail_to_wu('424662508@qq.com')
# if ss1 == 1:
# 	print("发送成功！")
# else:
# 	print("发送失败")


# def show():
# 	print('a')
# 	return [11, 22]
# 	print('b')
#
# show()

# 两个参数
def show(a1, a2):
	print(a1)
	print(a2)
show(111, 333)


# 默认参数
def show1(a1, a2=555):
	print(a1)
	print(a2)
show1(111)
show1(111, 333)
show1(a2=333, a1=111)


# 动态参数-元祖
def show2(*args):
	print(args, type(args))

show2(11, 22, 33, 44)


# 动态参数-列表
def show2(*args):
	print(args, type(args))

show2([11, 22, 33, 44])
l1 = [44, 55, 66, 77]
show2(* l1)
print('line:72'.center(30, '*'))


# 动态参数-字典
def show3(**kwargs):
	print(kwargs, type(kwargs))

show3(n1=11, n2=22)


# 动态参数-序列和字典
def show4(*args, **kwargs):
	print(args, type(args))
	print(kwargs, type(kwargs))


show4(11, 22, 33, n=44, m=55)

l = [11, 22, 33]
d = {'n': 44, 'm': 55}
# 直接传入会把l和d,传入*args
show4(l, d)

# 需要对传入的参数进行处理
show4(*l, **d)


# 用于字符串的格式化
str_tmp = "{0} is {1}!"
result = str_tmp.format('alex', 'humor')
print(result)

result = str_tmp.format(*['alex', 'humor'])
print(result)

str_tmp = "{name} is {actor}!"
d_tmp = {'name': 'alex', 'actor': 'humor'}
result = str_tmp.format(**d_tmp)
print(result)


# 简单函数lambda
func_tmp = lambda a: a+1
print(func_tmp(99))


