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

from conf import setting
from general_module import db_operater
from general_module import md5_encryption
from general_module import logger
from . import transaction_record
from . import login


# 信用卡支付接口
def check_out(arg):
	db_file = setting.ACCOUNT_DB
	info = db_operater.read_db(db_file)
	while True:
		card_id = input("请输入信用卡卡号（8位数字）：").strip()
		if re.match(r'^\d{8}$', card_id):
			if info.get(card_id, None):
				card_passwd = input("请输入密码：")
				if md5_encryption.md5_encryption(card_passwd) == info[card_id].get("password", None):
					if info[card_id]["current_limit"] - arg >= 0:
						info[card_id]["current_limit"] -= arg
						print("结算完成！")
						transaction_record.transaction_record(card_id, "消费", arg)
						db_operater.write_db(file=db_file, data=info)
						break
					else:
						print("余额不足！")
						break
				else:
					print("密码错误，请重新输入！")
			else:
				print("无效的卡号！请重新输入！")
		elif card_id == "B":
			break
		else:
			print("无效的输入！请重新输入！")


# 查询菜单
def check_info(card_id):
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	print("查询额度。。。")
	str_tmp = "您总额度为：{:.2f}，当前额度：{:.2f}，取现额度：{:.2f}, 余额：{:.2f}"
	print(str_tmp.format(db[card_id]["limit"], db[card_id]["current_limit"], db[card_id]["cash_limit"], db[card_id]["balance"]))


# 查询消费流水
def check_tran_record(card_id, start_date_str, end_date_str):
	print("这是查询消费流水的菜单。。。")
	# start_date_str = input("请输入开始时间(格式：%Y-%m-%d)：")
	# end_date_str = input("请输入结束时间(格式：%Y-%m-%d)：")
	try:
		# 将字符串格式的时间转换为日期格式
		start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
		end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
		# 定义消费记录数据库位置
		file_name = setting.RECORD_DB
		print("{}至{}的消费流水如下：".format(start_date_str, end_date_str))
		total_amount = 0
		with open(file_name, "r") as f:
			for line in f:
				# 按行读取字典
				d_temp = json.loads(line)
				# 按流水号检索
				for k in d_temp:
					if d_temp[k]["card_id"] == card_id:
						record_temp = d_temp[k]["tran_date"]
						if start_date <= record_temp <= end_date:
							print("交易时间：{} 交易详情：{} 交易金额：{} 卡号：{} 交易流水号：{}".format(
									d_temp[k]["tran_date"]), d_temp[k]["description"], d_temp[k]["rmb_amount"], d_temp[k]["card_id"], k)
							total_amount += d_temp[k]["rmb_amount"]
							return total_amount
	except ValueError:
		return None


# 账单详情:上个月22号到这个月21号的消费流水
def show_record(card_id):
	print("这是计算账单的功能。。。")
	# 将字符串格式的时间转换为日期格式
	today = datetime.date.today().timetuple()
	cur_year = today.tm_year
	cur_mon = today.tm_mon
	cur_day = today.tm_mday
	if cur_day >= 22:
		print("您本月账单已出。。。")
		last_mon = datetime.date(cur_year, cur_mon, 1) - datetime.timedelta(days=1)
		last_tm_mon = last_mon.timetuple().tm_mon   # 前一个月的月份
		last_tm_year = last_mon.timetuple().tm_year   # 前一个月的年份
		start_date_str = "{}-{}-{}".format(last_tm_year, last_tm_mon, 22)
		end_date_str = "{}-{}-{}".format(cur_year, cur_mon, 21)
		# 调用查询流水的菜单
		print("您本期账单{}至{}交易详情：".format(start_date_str, end_date_str))
		bill_amount = check_tran_record(card_id, start_date_str, end_date_str)
		print("本期应还：{}元。".format(bill_amount))
		db_file = setting.ACCOUNT_DB
		db = db_operater.read_db(db_file)
		db[card_id]["bill"] = bill_amount
		db_operater.write_db(file=db_file, data=db)
	else:
		print("您本月账单还没出。。。")


# 利息
def interest_amount(prin_amount, start_date_str, end_date_str):
	try:
		# 将字符串格式的时间转换为日期格式
		start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
		end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
		diff_days = end_date - start_date
		days = diff_days.days
		# 利滚利计算利息
		for i in range(days):
			prin_amount += prin_amount * 0.0005 * 1
		return prin_amount
	except TypeError:
		return None


# 计算利息
def get_interest():
	today = datetime.date.today()
	today_tm = today.timetuple()
	today_str = str(today)
	start_date = datetime.date(today_tm.tm_year, today_tm.tm_mon, 10)
	start_date_str = str(start_date)
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	if today_tm.tm_mday > 10:
		for i in db:
			# 逾期未还
			if db[i]["bill"] > 0:
				inter_amount = interest_amount(db[i]["bill"], start_date_str, today_str)
				# 记录交易流水
				transaction_record.transaction_record(i, "利息", inter_amount)


# 还款
def repay_bill(card_id):
	print("这是还款菜单。。。")
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
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
								print("您已成功还款{}元。".format(option3))
								logger.my_logger(card_id, "repayment {}.".format(option2))
								db_operater.write_db(file=db_file, data=db)
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
def transfer_accounts(card_id):
	print("这是转账菜单。。。")
	db_file = os.path.abspath(setting.ACCOUNT_DB)
	db = db_operater.read_db(db_file)
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
						loop_flag = False
						break
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
										logger.my_logger(card_id, "transfer to {} {}.".format(transfer_card_id, float(transfer_amount)))
										db_operater.write_db(file=db_file, data=db)
									elif option.upper() == "B":
										break
									elif option.upper() == "Q":
										loop_flag = False
										break
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
			break
		else:
			print("两次输入的卡号不一致或卡号有误，请重新输入！")


# 提现
def enchashment(card_id):
	print("这是取现的菜单。。。")
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	loop_flag = True
	while loop_flag:
		print("您目前的取现额度是：{:.2f}元".format(db[card_id]["cash_limit"]))
		cash_amount = input("请输入金额（100的整数），手续费5%，Q退出：").strip()
		if cash_amount.isdigit():
			cash_amount = float(cash_amount)
			if cash_amount % 100 == 0:
				handle_charge = cash_amount * 0.05
				print("您此次取款：{:.2f}元，手续费：{:.2f}元。".format(cash_amount, handle_charge))
				all_amount = cash_amount + handle_charge
				while loop_flag:
					option = input("1确认，B返回，Q退出").strip()
					if option == "1":
						db[card_id]["limit"] -= all_amount
						db[card_id]["cash_limit"] -= all_amount
						db[card_id]["current_limit"] -= all_amount
						# db[card_id]["bill"] += all_amount
						# 记录交易流水
						transaction_record.transaction_record(card_id, "取现", cash_amount)
						transaction_record.transaction_record(card_id, "手续费", handle_charge)
						logger.my_logger(card_id, "withdrawal {}, handle charge {}.".format(cash_amount, handle_charge))
						# 回写数据
						db_operater.write_db(file=db_file, data=db)
					elif option.upper() == "B":
						break
					elif option.upper() == "Q":
						loop_flag = False
						break
			else:
				print("无效输入，请重新输入！")
		elif cash_amount.upper() == "Q":
			break
		else:
			print("无效的输入，请重新输入！")


# 修改密码
def change_password(card_id):
	print("这是修改密码的菜单。。。")
	# 输入原密码次数是否应该有限制？
	db_file = setting.ACCOUNT_DB
	db = db_operater.read_db(db_file)
	loop_flag = True
	while loop_flag:
		password = input("请输入原密码，Q退出：").strip()
		if md5_encryption.md5_encryption(password) == db[card_id]["password"]:
			new_password_1 = input("请输入新密码：").strip()
			new_password_2 = input("请再次输入新密码：").strip()
			bool_a = new_password_1 == new_password_2
			bool_b = new_password_1.isdigit()
			bool_c = len(new_password_1) == 6
			if all([bool_a, bool_b, bool_c]):
				new_password = new_password_1
				while loop_flag:
					option = input("1确认，B返回，Q退出：").strip()
					if option == "1":
						db[card_id]["password"] = md5_encryption.md5_encryption(new_password)
						logger.my_logger(card_id, "change password.")
						print("密码修改完成！")
						# 回写数据
						db_operater.write_db(file=db_file, data=db)
					elif option.upper() == "B":
						break
					elif option.upper() == "Q":
						loop_flag = False
						break
			else:
				print("两次密码不一致，或输入的密码不是6位数字！")
		elif password.upper() == "Q":
			break
		else:
			print("密码错误，请重试！")


# 用户界面
@login.login(1)
def main_body(card_id):
	print("这是用户界面：")
	logger.my_logger(card_id, "log in.")
	# 先看有没有产生利息。。。
	get_interest()
	loop_flag = True
	while loop_flag:
		option = input("1.查询 2.还款 3.转账 4.提现 5.修改密码 Q.退出：").strip()
		if option == "1":
			print("欢迎进入查询系统：")
			while loop_flag:
				option2 = input("1.查询额度 2.查询账单 3.查询交易流水 B返回Q退出：").strip()
				if option2 == "1":
					check_info(card_id)
					logger.my_logger(card_id, "查询额度")
				elif option2 == "2":
					show_record(card_id)
					logger.my_logger(card_id, "查询账单")
				elif option2 == "3":
					while loop_flag:
						print("请输入要查询的起始日期：")
						start_date_str = input("开始日期：").strip()
						end_date_str = input("结束日期：").strip()
						a = check_tran_record(card_id, start_date_str, end_date_str)
						logger.my_logger(card_id, "check the transactions flowing water from {} to {}.".format(start_date_str, end_date_str))
						if not a:
							break
				elif option2.upper() == "B":
					break
				elif option2.upper() == "Q":
					loop_flag = False
					break
				else:
					print("无效的输入！")
		elif option == "2":
			logger.my_logger(card_id, "还款")
			# 还款
			repay_bill(card_id)
		elif option == "3":
			transfer_accounts(card_id)
		elif option == "4":
			enchashment(card_id)
		elif option == "5":
			change_password(card_id)
		elif option.upper() == "Q":
			logger.my_logger(card_id, "log out.")
			loop_flag = False
		else:
			print("无效的输入！")


# info = {
# 	"88888881":
# 		{"name": "alex", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 20000,
# 			"cash_limit": 10000, "current_limit": 20000, "bill": 8888, "balance": 1000, "retry_count": 0, "created_date": datetime.date(2016, 2, 1)},
# 	"88888882":
# 		{"name": "john", "lock_flag": 0, "password": "b8b28fcfe009057f2ef7362b1e91fe7a", "limit": 10000,
# 			"cash_limit": 5000, "current_limit": 10000, "bill": 0, "balance": 0, "retry_count": 0, "created_date": datetime.date(2016, 2, 2)},
# }
def main():
	main_body()

if __name__ == "__main__":
	main()


# check_info("88888881", info)
# a = repay_bill("88888881", info)
# a = transfer_accounts("88888881", info)
# a = enchashment("88888881", info)
# a = change_password("88888881", info)
#
# for i in a:
# 	print(a[i])
