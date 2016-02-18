#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
信用卡的主程序
"""

import admin_menu
import user_menu


def card_main():
	print("这是ATM登录程序！")
	loop_flag = True
	while loop_flag:
		option = input("1.普通用户登录 2.管理员登录 Q.退出：").strip()
		if option == "1":
			user_menu.main_body()
		elif option == "2":
			admin_menu.main_body()
		elif option.upper() == "Q":
			break
		else:
			print("无效的输入！")


def main():
	card_main()

if __name__ == "__main__":
	main()
