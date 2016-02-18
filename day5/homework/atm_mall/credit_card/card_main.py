#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
信用卡的主程序
"""

from . import admin_menu
from . import user_menu


def card_main():
	print("这是ATM登录程序！")
	loop_flag = True
	while loop_flag:
		option = input("1.普通用户登录 2.管理员登录 Q.退出：").strip()
		if option == "1":
			print("这是普通用户登录界面：")
			user_menu.main_body()
		elif option == "2":
			print("这是管理员登录界面：")
			admin_menu.main_body()
		elif option.upper() == "Q":
			break
		else:
			print("无效的输入！")


def main():
	card_main()

if __name__ == "__main__":
	main()
