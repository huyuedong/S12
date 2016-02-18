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
from conf import setting
from general_module import db_operater
from general_module import logger
from . import login


# 调整额度
def change_limit(admin_id):
	print("这是调整额度的菜单。。。")
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
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
						logger.my_logger(card_number, "额度被管理员{}调整为{}。".format(admin_id, db[card_number]["limit"]))
						db_operater.write_db(file=db_file, data=db)
					elif option2.upper() == "B":
						break
					elif option2.uooer() == "Q":
						loop_flag = False
						break
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					loop_flag = False
					break
				else:
					print("无效的输入，请重新输入！")
		elif card_number.upper() == "Q":
			break
		else:
			print("卡号不存在请重新输入！")


# 添加账户
def add_card_account(admin_id):
	print("这是添加信用卡账户的菜单。。。")
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	loop_flag = True
	while loop_flag:
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
			db_demo[card_id]["limit"] = float(card_limit)
			db_demo[card_id]["current_limit"] = float(card_limit)
			db_demo[card_id]["cash_limit"] = float(db_demo[card_id]["current_limit"] * 0.5)
			db_demo[card_id]["lock_flag"] = 0
			db_demo[card_id]["password"] = "b8b28fcfe009057f2ef7362b1e91fe7a"
			db_demo[card_id]["bill"] = 0
			db_demo[card_id]["balance"] = 0
			db_demo[card_id]["retry_count"] = 0
			db_demo[card_id]["created_date"] = datetime.date.today()
			while loop_flag:
				option = input("确认添加按1，B返回Q退出：")
				if option == "1":
					print("正在添加。。。")
					db.update(db_demo)  # 更新数据
					print("添加完成！")
					logger.my_logger("管理员{}", "添加账户，卡号：{}".format(admin_id, card_id))
					db_operater.write_db(file=db_file, data=db)
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					loop_flag = False
					break
				else:
					print("无效的输入，请重新输入！")
		elif card_name.upper() == "Q":
			break
		else:
			print("无效的输入，请重新输入！")


# 冻结账户
def frozen_account(admin_id):
	print("这是冻结账户菜单。。。")
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	loop_flag = True
	while loop_flag:
		card_number = input("请输入要冻结的卡号（Q退出）：").strip()
		if db.get(card_number):
			print("卡号：{}，姓名：{}，当前账单：{}".format(card_number, db[card_number]["name"], db[card_number]["bill"]))
			while loop_flag:
				option = input("确认冻结按1，B返回，Q退出：").strip()
				if option == "1":
					db[card_number]["lock_flag"] = 1
					logger.my_logger(card_number, "被管理员{}冻结".format(admin_id))
					db_operater.write_db(file=db_file, data=db)
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					loop_flag = False
					break
				else:
					print("无效的输入，请重新输入！")
		elif card_number.upper() == "Q":
			break
		else:
			print("卡号不存在，请重新输入！")


# 重置密码
def reset_password(admin_id):
	print("这是重置密码菜单。。。")
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	loop_flag = True
	while loop_flag:
		card_number = input("请输入要重置密码的卡号,Q退出：").strip()
		if card_number.upper() == "Q":
			break
		elif all([card_number.isdigit(), db.get(card_number)]):
			while loop_flag:
				option = input("您要重置密码的卡号为{},用户名为{}，1确认，B返回，Q退出！".format(card_number, db[card_number]["name"]))
				if option == "1":
					db[card_number]["password"] = "b8b28fcfe009057f2ef7362b1e91fe7a"
					print("卡号：{}的密码已重置为初始密码！".format(card_number))
					logger.my_logger(card_number, "被管理员{}重置为初始密码。".format(admin_id))
					db_operater.write_db(file=db_file, data=db)
				elif option.upper() == "B":
					break
				elif option.upper() == "Q":
					loop_flag = False
					break
				else:
					print("无效的输入，请重新输入！")
		else:
			print("无效的输入，请重新输入！")


# 管理员界面
@login.login(2)
def main_body(admin_id):
	print("欢迎来到管理员操作界面！")
	loop_flag = True
	while loop_flag:
		option = input("1.调整额度 2.添加账户 3.冻结账户 4.重置密码 Q.退出：").strip()
		if option == "1":
			change_limit(admin_id)
		elif option == "2":
			add_card_account(admin_id)
		elif option == "3":
			frozen_account(admin_id)
		elif option == "4":
			reset_password(admin_id)
		elif option.upper() == "Q":
			loop_flag = False
		else:
			print("无效的输入！")


def main():
	main_body()


if __name__ == "__main__":
	main()


# info = {
# 	"88888881":
# 		{"name": "alex", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 20000,
# 			"cash_limit": 10000, "current_limit": 20000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
# 	"88888882":
# 		{"name": "john", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 10000,
# 			"cash_limit": 5000, "current_limit": 10000, "bill": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
# }

# a = change_limit(info)
# a = add_card_account(info)
# a = frozen_account(info)
# a = reset_password(info)
#
# for i in a:
# 	print(a[i])
