#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
'''
    编写登陆接口
        -输入用户名和密码
        -认证成功后显示欢迎信息
        -输错三次密码锁定相应用户
'''

account_file = "account.txt"    # 定义用于存储用户名和密码的account.txt
lock_file = "lock.txt"      # 定义用于存储锁定用户名的lock.txt
lock_list = []
account_list = []
is_not_locked = False
login_success = False

user_name = input("Please input your username:").strip()    # 获取输入的用户名（去掉空格）
with open(lock_file) as f1:
    for i in f1.readlines():
        i.strip()    # 去掉空格
        lock_list.append(i)
if user_name in lock_list:  # 判断是否为锁定用户
    print("Sorry, %s! You were locked!" % user_name)    # 提示用户为锁定用户
    is_not_locked = True
while is_not_locked:    # 不是锁定用户时继续执行下面程序
    with open(account_file) as f2:
        for line in f2.readlines():
            account_list.append(line.split())    # 将account.txt文件中的每一行去掉换行符写入account_list
    for i in account_list:
        if user_name == i[0]:
            for j in range(3):    # 提供三次输入密码的机会
                pass_word = input("Please input your password:")    # 获取输入的密码
                if pass_word == i[1]:
                    print("%s,Welcome to login !" % user_name)    # 密码正确打印欢迎信息
                    login_success = True
                    break    # 跳出子循环
            if login_success:
                break    # 跳出父循环
            else:    # 三次输错密码，用户锁定
                with open(lock_file, 'at') as f3:   # 将输错三次密码的用户名写入lock.txt
                    f3.write('%s\n' % user_name)
                print("Too many retry,%s will be locked!" % user_name)    # 打印提示用户已经被锁定
                break
    else:    # 输入的用户名没有注册时，打印提示信息
        print("Sorry,%s you haven't registered!" % user_name)
        break
