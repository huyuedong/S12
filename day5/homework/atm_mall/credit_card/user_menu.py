#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
用户操作
-查询额度、账单
-还款
-转账
-提现
-修改密码
"""

import datetime


# 查询菜单
def check_info(card_id, db):
	print("这是查询额度、账单菜单。。。")
	while True:
		option = input("1查询额度，2查询账单，Q退出！：").strip()
		if option == "1":
			print("查询额度。。。")
			print("您总额度为：{}，当前额度：{}，取现额度：{}".format(db[card_id]["limit"], db[card_id]["current_limit"], db[card_id]["cash_limit"]))
		elif option == "2":
			print("查询账单。。。")
			print("您当前的账单为：{}".format(db[card_id]["bill"]))
		elif option.upper() == "Q":
			break
		else:
			print("无效的输入，请重新输入！")


# 还款
def repay_bill(card_id, db):
	print("这是还款菜单。。。")
	loop_flag = True
	while loop_flag:
		option = input("1：自己还款，2：替别人还款，3：退出").strip()
		if option == "1":
			while loop_flag:
				bill = db[card_id]["bill"]
				print("您当前账单为：{}".format(bill))
				option2 = input("请输入您要还款的金额：").strip()
				if option2.isdigit():
					if int(option2) > int(bill):
						while loop_flag:
							print("多余的钱也没有利息哦~")
							# 用临时变量存储
							bill_temp = 0
							current_limit_demo = int(option2) - int(bill)
							option3 = input("你账单：{}，本次还款：{}，1确认，B返回，Q退出：".format(bill, option2))
							if option3 == "1":
								db[card_id]["bill"] = bill_temp
								db[card_id]["current_limit"] = current_limit_demo
								return db
							elif option3.upper() == "B":
								break
							elif option3.upper() == "Q":
								return db
							else:
								print("无效的输入，请重新输入！")
					elif int(option2) == 0:
						print("别逗了，你丫根本没放钱进来。。。")
					else:
						while loop_flag:
							bill_temp = bill - int(option2)
							print("你本次还款：{}元，剩余账单：{}元".format(option2, bill_temp))
							option4 = input("1确认还款，B返回，Q退出：")
							if option4 == "1":
								db[card_id]["bill"] = bill_temp
								return db
							elif option4.upper() == "B":
								break
							elif option4.upper() == "Q":
								return db
							else:
								print("无效的输入，请重新输入！")
				elif option2.upper() == "B":
					break
				elif option2.upper() == "Q":
					return db
				else:
					print("无效的输入，请重新输入！")
		elif option == "2":
			pass
		elif option.upper() == "Q":
			return db
		else:
			print("无效的输入，请重新输入！")


# 转账
def transfer_accounts(db):
	print("这是转账菜单。。。")


# 提现
def enchashment(db):
	print("这是取现的菜单。。。")


# 修改密码
def change_password():
	print("这是修改密码的菜单。。。")


info = {
	"88888881":
		{"name": "alex", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 20000,
			"cash_limit": 10000, "current_limit": 20000, "bill": 8888, "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
	"88888882":
		{"name": "john", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 10000,
			"cash_limit": 5000, "current_limit": 10000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
}

# check_info("88888881", info)
a = repay_bill("88888881", info)
for i in a:
	print(a[i])
