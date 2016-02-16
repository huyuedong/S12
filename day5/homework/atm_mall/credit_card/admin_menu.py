#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
管理员操作
-调整额度
-添加账户
-冻结账户
-重置密码
"""
import datetime
import re


# 调整额度
def change_limit(db):
	print("这是调整额度的菜单。。。")
	loop_flag = True
	while loop_flag:
		card_number = input("请输入要操作的卡号（Q退出）：").strip()
		if db.get(card_number):
			print("{}原额度是{}。".format(card_number, db[card_number]["limit"]))
			while loop_flag:
				option = input("请输入调整后的额度，（Q退出B返回上级）：").strip()
				if option.isdigit():
					option2 = input("确认修改请按1，（Q退出B返回上级）：").strip()
					if option2 == "1":
						db[card_number]["limit"] = int(option)
						print("卡号{}的额度修改为{}。".format(card_number, db[card_number]["limit"]))
						return db
					elif option2.upper() == "B":
						break
					elif option2.uooer() == "Q":
						return db
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					return db
				else:
					print("无效的输入，请重新输入！")
		elif card_number.upper() == "Q":
			return db
		else:
			print("卡号不存在请重新输入！")


# 添加账户
def add_card_account(db):
	print("这是添加信用卡账户的菜单。。。")
	while True:
		db_demo = {}
		card_id = format(len(db)+1, "8=8")  # 生成一个8位的卡号
		db_demo[card_id] = {}
		card_name = input("请输入卡主姓名,Q退出：").strip()
		card_limit = input("请输入卡片额度：").strip()
		bool_a = re.match(r'^[a-zA-Z.]{4,26}$', card_name)  # 英文名字4-26位
		bool_b = re.match(r'^[\u4e00-\u9fa5]{2,4}$', card_name)    # 中文名字2-4位
		bool_c = re.match(r'^\d{1,8}$', card_limit)
		if all([(bool_a or bool_b), bool_c]):
			# 初始化用户信息
			db_demo[card_id]["name"] = card_name
			db_demo[card_id]["limit"] = int(card_limit)
			db_demo[card_id]["current_limit"] = int(card_limit)
			db_demo[card_id]["cash_limit"] = int(db_demo[card_id]["current_limit"] * 0.5)
			db_demo[card_id]["lock_flag"] = 0
			db_demo[card_id]["password"] = "b8b28fcfe009057f2ef7362b1e91fe7a"
			db_demo[card_id]["bill"] = 0
			db_demo[card_id]["balance"] = 0
			db_demo[card_id]["retry_count"] = 0
			db_demo[card_id]["created_date"] = datetime.date.today()
			while True:
				option = input("确认添加按1，B返回Q退出：")
				if option == "1":
					print("正在添加。。。")
					db.update(db_demo)  # 更新数据
					print("添加完成！")
					return db
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					return db
				else:
					print("无效的输入，请重新输入！")
		elif card_name.upper() == "Q":
			return db
		else:
			print("无效的输入，请重新输入！")


# 冻结账户
def frozen_account(db):
	print("这是冻结账户菜单。。。")
	loop_flag = True
	while loop_flag:
		card_number = input("请输入要冻结的卡号（Q退出）：").strip()
		if db.get(card_number):
			print("卡号：{}，姓名：{}，当前账单：{}".format(card_number, db[card_number]["name"], db[card_number]["bill"]))
			while loop_flag:
				option = input("确认冻结按1，B返回，Q退出：").strip()
				if option == "1":
					db[card_number]["lock_flag"] = 1
					return db
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					return db
				else:
					print("无效的输入，请重新输入！")
		elif card_number.upper() == "Q":
			return db
		else:
			print("卡号不存在，请重新输入！")


# 重置密码
def reset_password(db):
	print("这是重置密码菜单。。。")
	while True:
		card_number = input("请输入要重置密码的卡号,Q退出：").strip()
		if card_number.upper() == "Q":
			return db
		elif all([card_number.isdigit(), db.get(card_number)]):
			while True:
				option = input("您要重置密码的卡号为{},用户名为{}，1确认，B返回，Q退出！".format(card_number, db[card_number]["name"]))
				if option == "1":
					db[card_number]["password"] = "b8b28fcfe009057f2ef7362b1e91fe7a"
					print("卡号：{}的密码已重置为初始密码！".format(card_number))
					return db
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					return db
				else:
					print("无效的输入，请重新输入！")
		else:
			print("无效的输入，请重新输入！")

info = {
	"88888881":
		{"name": "alex", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 20000,
			"cash_limit": 10000, "current_limit": 20000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
	"88888882":
		{"name": "john", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 10000,
			"cash_limit": 5000, "current_limit": 10000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
}

a = change_limit(info)
# a = add_card_account(info)
# a = frozen_account(info)
# a = reset_password(info)

for i in a:
	print(a[i])
