#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
day8 homework test
"""

config = {
	"default": [],
	"db": [
		"172.18.26.193",
		"192.168.183.131",
	],
	"nginx": [
		"172.18.26.193",
	],
	"tomcat": [
		"192.168.183.131",
	],
}

# print(config.keys())
# print("db" in config.keys())
#
# l1 = ["db", "tomcat"]

config["nginx"].append("172.18.26.193")

# for k in config:
# 	print(k, config[k])
# 	config[k] = list(set(config[k]))
# 	print(k, config[k])
# print("=============================")
# if "nginx" in config:
# 	config.pop("nginx")
# config.pop("default")
# for k in config:
# 	print(k, config[k])
# print("=" * 50)
# test_list = ["123.123.123.123", "192.168.183.131", ]
# for k in config:
# 	for j in test_list:
# 		if j in config[k]:
# 			config[k].remove(j)
pop_list = []
j = "172.18.26.193"
for k in config:
	print(k, config[k])
	if j in config[k]:
		pop_list.append({k: j})
print(pop_list)

# if "172.18.26.193" in config.get("abc", []):
#
# 	print("yes!")
# else:
# 	print("no!")

