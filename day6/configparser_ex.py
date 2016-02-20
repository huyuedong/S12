#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
"""
configparser 练习
"""

import configparser

# 写一个配置文件
# config = configparser.ConfigParser()
# config["DEFAULT"] = {'ServerAliveInterval': '45', 'Compression': 'yes', 'CompressionLevel': '9'}
#
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
# 	config.write(configfile)

# 读配置文件
# config = configparser.ConfigParser()
# print(config.sections())
# a = config.read("test.cfg")
# print(a)
# print(config.sections())
# print("bitbucket.org" in config.sections())
# print(config["bitbucket.org"]["user"])
#
# for key in config["bitbucket.org"]:
# 	print(key, config["bitbucket.org"][key])

# 增删改查
config = configparser.ConfigParser()
config.read("test.cfg")
sec = config.sections()
print(sec)

options = config.options("bitbucket.org")
print(options)

item_list = config.items("bitbucket.org")
print(item_list)

val = config.get("bitbucket.org", "compressionlevel")
print(val)
val = config.getint("bitbucket.org", "compressionlevel")
print(val)

# 改写
config.remove_section("bitbucket.org")
config.write(open("test2.cfg", "w"))

sec = config.has_section("bitbuckrt.org")
print(sec)
config.add_section("bitbucket.org")
sec = config.has_section("bitbuckrt.org")
print(sec)

config.write(open("test2.cfg", "w"))

config.set("bitbucket.org", 'k1', "11111")
config.write(open("test2.cfg", "w"))

config.remove_option("topsecret.server.com", "port")
config.write(open("test2.cfg", "w"))
