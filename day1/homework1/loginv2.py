#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
	编写登陆接口
		-输入用户名和密码
		-认证成功后显示欢迎信息
		-输错三次密码锁定相应用户
		* 在第一版的基础上修复了分两次判断用户名和密码的bug,因为实际的登陆程序都是一次判断用户名和密码
"""

account_file = "account.txt"
lock_file = "lock.txt"
account_list = []
lock_list = []
retry_counts = 0
max_retry_counts = 3
login_success = False
is_locked = False


# 初始化用户信息
def init_account_info():
	with open(account_file, 'r') as f:
		for account_info in f.readlines():
			account_info = account_info.strip()
			account_list.append(account_info.split())
	return account_list


# 初始化锁定用户信息
def init_lock_account_info():
	with open(lock_file, 'r') as f2:
		for line in f2.readlines():
			lock_list.append(line.strip())
	return lock_list


# 锁定用户操作
def lock_account():
	with open(lock_file, 'at') as f:
		f.write("%s\n" % user_name)


# 主程序
while retry_counts < max_retry_counts:
	while not login_success and not is_locked:
		init_account_info()
		init_lock_account_info()
		user_name = input("Please input your username：").strip()
		pass_word = input("Please input your password：").strip()
		if user_name in lock_list:
			print("Sorry,your username were locked!")
			is_locked = True
			break
		else:
			for j in account_list:
				if j[0] == user_name and j[1] == pass_word:
					print("Welcome to login!")
					login_success = True
					break
			# 找不到用户名或密码错误
			else:
				print("username or password wrong! please retry!")
				retry_counts += 1
				break
		# 跳出第二层while循环
		if login_success or is_locked:
			break
	# 跳出第一层while循环
	if login_success or is_locked:
		break
	# 密码输入超过三次锁定用户
else:
	print("Sorry,too many retry! Your username will be locked!")
	lock_account()
