#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

# for i in range(3):
# 	flag = False
# 	user = input("请输入账号：")
# 	passwd = input("请输入密码：")
# 	with open("user_passwd", "r") as f:
# 		for line in f:
# 			line = line.strip("\n")
# 			if line.split()[0] == user and line.split()[1] == passwd:
# 				print("欢迎登陆")
# 				flag = True
# 				break
# 		else:
# 			print("您输入的账号不存在或密码错误")
# 	if flag:
# 		break
# else:
# 	print("您尝试过多，已被锁定")

m1 = {}
dic_a = {
	"山东": ["1", "2"],
	"江苏": ["3", "4"],
	"福建": ["5", "6"],
}
for i in range(len(dic_a)):
	m1.setdefault(i)
for key in m1:
	for j in dic_a:
		m1[key] = j
print(m1)

list_temp = []
for aa in dic_a.items():
	list_temp.append({aa[0]: aa[1]})

dic = dict(enumerate([{x[0]: x[1]} for x in dic_a.items()], 1))

dic1 = dict(enumerate(iter({x[0]: x[1]} for x in dic_a.items()), 1))
print(dic1)
print(dic)

print(list(iter(dic_a.items())))

# dic = dict(enumerate([lambda x, y:{x: y}, dic_a.items()], 1))
# print(dic)
#
# a = [lambda x: {x[0]: x[1]} for x in dic_a.items()]
# print(a)
#
# for aa in dic_a.items():
# 	print({aa[0]: aa[1]})

