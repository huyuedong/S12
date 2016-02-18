#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
主程序
"""

# import credit_card
# import mall


from mall import shopping_mall
from credit_card import card_main


def main():
	loop_flag = True
	while loop_flag:
		option = input("1.购物商城 2.ATM Q.退出：").strip()
		if option == "1":
			shopping_mall.main()
		elif option == "2":
			card_main.card_main()
		elif option == "Q":
			loop_flag = False
		else:
			print("无效的输入！")


if __name__ == "__main__":
	main()
