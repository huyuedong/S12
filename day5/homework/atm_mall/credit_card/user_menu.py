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
import re
import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from general_module import md5_encryption


# 查询菜单
def check_info(card_id, db):
	print("这是查询额度、账单菜单。。。")
	while True:
		option = input("1查询额度，2查询账单，Q退出！：").strip()
		if option == "1":
			print("查询额度。。。")
			print("您总额度为：{:.2f}，当前额度：{:.2f}，取现额度：{:.2f}".format(db[card_id]["limit"], db[card_id]["current_limit"], db[card_id]["cash_limit"]))
		elif option == "2":
			print("查询账单。。。")
			print("您当前的账单为：{:.2f}".format(db[card_id]["bill"]))
		elif option.upper() == "Q":
			break
		else:
			print("无效的输入，请重新输入！")


# 查询消费流水
def check_tran_record(card_id):
	print("这是查询消费流水的菜单。。。")
	start_date_str = input("请输入开始时间(格式：%Y-%m-%d)：")
	end_date_str = input("请输入结束时间(格式：%Y-%m-%d)：")
	try:
		# 将字符串格式的时间转换为日期格式
		start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
		end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
		# 定义消费记录数据库位置
		base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		file_name = "{}\\database\\record.db".format(base_path)
		with open(file_name, "r") as f:
			for line in f:
				# 按行读取字典
				d_temp = json.loads(line)
				# 按流水号检索
				for k in d_temp:
					if d_temp[k]["card_id"] == card_id:
						record_temp = d_temp[k]["tran_date"]
						print("{}至{}的消费流水如下：".format(start_date_str, end_date_str))
						if start_date <= record_temp <= end_date:
							print("交易时间：{} 交易详情：{} 交易金额：{} 卡号：{} 交易流水号：{}".format(
									d_temp[k]["tran_date"]), d_temp[k]["description"], d_temp[k]["rmb_amount"], d_temp[k]["card_id"], k)
	except ValueError:
		return None


# 账单详情
def show_record():
	print("这是计算账单的功能。。。")
	# 将字符串格式的时间转换为日期格式
	start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
	end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
	# 定义消费记录数据库位置
	base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	file_name = "{}\\database\\record.db".format(base_path)
	with open(file_name, "r") as f:
		for line in f:
			# 按行读取字典
			d_temp = json.loads(line)
			# 按流水号检索
			for k in d_temp:
				if d_temp[k]["card_id"] == card_id:
					record_temp = d_temp[k]["tran_date"]
					print("{}至{}的消费流水如下：".format(start_date_str, end_date_str))
					if start_date <= record_temp <= end_date:
						print("交易时间：{} 交易详情：{} 交易金额：{} 卡号：{} 交易流水号：{}".format(
								d_temp[k]["tran_date"]), d_temp[k]["description"], d_temp[k]["rmb_amount"], d_temp[k]["card_id"], k)



# 还款
def repay_bill(card_id, db):
	print("这是还款菜单。。。")
	loop_flag = True
	while loop_flag:
		option = input("1：自己还款，2：替别人还款，3：退出").strip()
		if option == "1":
			while loop_flag:
				bill = db[card_id]["bill"]
				print("您当前账单为：{:.2f}".format(bill))
				option2 = input("请输入您要还款的金额：").strip()
				if re.match(r'^\d+\.?\d{1,2}$', option2):
					option2 = float(option2)
					if option2 > float(bill):
						while loop_flag:
							# 用临时变量存储
							bill_temp = 0
							balance_temp = option2 - float(bill)    # 多的钱存入余额
							current_limit_add_temp = option2 - float(bill)   # 余额也算到当前额度里
							option3 = input("你账单：{:.2f}元，本次还款：{:.2f}元，1确认，B返回，Q退出：".format(bill, option2)).strip()
							if option3 == "1":
								db[card_id]["bill"] = bill_temp    # 还完后账单清零
								db[card_id]["balance"] = balance_temp   # 余额
								db[card_id]["current_limit"] += current_limit_add_temp  # 当前额度
								return db
							elif option3.upper() == "B":
								break
							elif option3.upper() == "Q":
								return db
							else:
								print("无效的输入，请重新输入！")
					elif option2 == 0:
						print("别逗了，你丫根本没放钱进来。。。")
					else:
						while loop_flag:
							bill_temp = bill - float(option2)
							print("你本次还款：{:.2f}元，剩余账单：{:.2f}元".format(option2, bill_temp))
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
			pass    # 功能类似于转账，此处略。。。
		elif option.upper() == "Q":
			return db
		else:
			print("无效的输入，请重新输入！")


# 转账
def transfer_accounts(card_id, db):
	print("这是转账菜单。。。")
	loop_flag = True
	while loop_flag:
		card_id_1 = input("请输入卡号，Q退出：").strip()
		card_id_2 = input("请再次输入卡号：").strip()
		bool_a = card_id_1 == card_id_2
		bool_b = card_id_1.isdigit()
		bool_c = card_id_2.isdigit()
		bool_d = db.get(card_id_2)  # 暂时只支持同行转账
		if all([bool_a, bool_b, bool_c, bool_d]):
			transfer_card_id = card_id_1
			if transfer_card_id != card_id:
				while loop_flag:
					print("您当前余额：{:.2f}元。".format(db[card_id]["balance"]))
					print("您要转账的卡号是：{}".format(transfer_card_id))
					transfer_amount = input("请输入要转账的金额，B返回Q退出：").strip()
					if transfer_amount.upper() == "B":
						break
					elif transfer_amount.upper() == "Q":
						return db
					elif transfer_amount.isdigit():
						# 要转账 金额肯定要大于0
						if float(transfer_amount) > 0:
							if db[card_id]["balance"] >= float(transfer_amount):
								print("您要向{}账户转账{:.2f}元。。。".format(transfer_card_id, float(transfer_amount)))
								while loop_flag:
									option = input("1确认，B返回，Q退出！").strip()
									if option == "1":
										db[card_id]["balance"] -= float(transfer_amount)  # 从自己卡的余额里减掉转账的金额
										db[transfer_card_id]["balance"] += float(transfer_amount)    # 把转账的金额加到对方卡的余额
										return db
									elif option.upper() == "B":
										break
									elif option.upper() == "Q":
										return db
									else:
										print("无效的输入，请重新输入！")
							else:
								print("您的余额不足，请充值后再试！")
						else:
							print("别捣乱。。。")
					else:
						print("无效的输入，请重新输入！")
			else:
				print("自己不能给自己转账。。。")
		elif card_id_1.upper() == "Q":
			return db
		else:
			print("两次输入的卡号不一致或卡号有误，请重新输入！")


# 提现
def enchashment(card_id, db):
	print("这是取现的菜单。。。")
	while True:
		print("您目前的取现额度是：{:.2f}元".format(db[card_id]["cash_limit"]))
		cash_amount = input("请输入金额（100的整数），手续费5%，Q退出：").strip()
		if cash_amount.isdigit():
			cash_amount = float(cash_amount)
			if cash_amount % 100 == 0:
				handle_charge = cash_amount * 0.05
				print("您此次取款：{:.2f}元，手续费：{:.2f}元。".format(cash_amount, handle_charge))
				all_amount = cash_amount + handle_charge
				while True:
					option = input("1确认，B返回，Q退出").strip()
					if option == "1":
						db[card_id]["limit"] -= all_amount
						db[card_id]["cash_limit"] -= all_amount
						db[card_id]["current_limit"] -= all_amount
						db[card_id]["bill"] += all_amount
						return db
					elif option.upper() == "B":
						break
					elif option.upper() == "Q":
						return db
			else:
				print("无效输入，请重新输入！")
		elif cash_amount.upper() == "Q":
			return db
		else:
			print("无效的输入，请重新输入！")


# 修改密码
def change_password(card_id, db):
	print("这是修改密码的菜单。。。")
	# 输入原密码次数是否应该有限制？
	while True:
		password = input("请输入原密码，Q退出：").strip()
		if md5_encryption.md5_encryption(password) == db[card_id]["password"]:
			new_password_1 = input("请输入新密码：").strip()
			new_password_2 = input("请再次输入新密码：").strip()
			bool_a = new_password_1 == new_password_2
			bool_b = new_password_1.isdigit()
			bool_c = len(new_password_1) == 6
			if all([bool_a, bool_b, bool_c]):
				new_password = new_password_1
				while True:
					option = input("1确认，B返回，Q退出：").strip()
					if option == "1":
						db[card_id]["password"] = md5_encryption.md5_encryption(new_password)
						print("密码修改完成！")
						return db
					elif option.upper() == "B":
						break
					elif option.upper() == "Q":
						return db
			else:
				print("两次密码不一致，或输入的密码不是6位数字！")
		elif password.upper() == "Q":
			return db
		else:
			print("密码错误，请重试！")


info = {
	"88888881":
		{"name": "alex", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 20000,
			"cash_limit": 10000, "current_limit": 20000, "bill": 8888, "balance": 1000, "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
	"88888882":
		{"name": "john", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 10000,
			"cash_limit": 5000, "current_limit": 10000, "bill": 0, "balance": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
}

# check_info("88888881", info)
# a = repay_bill("88888881", info)
# a = transfer_accounts("88888881", info)
# a = enchashment("88888881", info)
a = change_password("88888881", info)

for i in a:
	print(a[i])
