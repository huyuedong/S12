#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
主程序
"""

# from credit_card import admin_menu
# from credit_card import transaction_record
# from credit_card import user_menu
# from general_module import db_operater
# from general_module import logger
# from general_module import md5_encryption
from mall import mall_login
# from mall import mall_register
from mall import shopping_mall


def main():
	loop_flag = True
	while loop_flag:
		option = input("1:购物商城 2：ATM 3：退出").strip()
		if option == "1":
			shopping_mall.main()
		elif option == "2":
			pass
		elif option == "3":
			loop_flag = False
		else:
			print("无效的输入！")


if __name__ == "__main__":
	main()
