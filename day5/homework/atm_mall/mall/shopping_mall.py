#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
购物商城
"""

from collections import OrderedDict
from collections import Counter

shop_dic = {"MacBook Air": 7999, "Starbucks Coffee": 33, "iphone 6 Plus": 6188, "Air Jordan S.F 4": 888, "Casio": 1799}
shopping_cart_list = []


# 获取用户的预算
def get_budget():
	while True:
		user_budget = input("请输入您的预算：").strip()    # 获取用户输入的预算
		if user_budget.isdigit():
			user_budget = int(user_budget)
			return user_budget
		else:
			print("无效的输入请重新输入！")


# 初始化商品目录
def init_shop_dic(dic):
	print("Welcome to Q1mi's shopping mall,below are the things we are selling:")
	return OrderedDict(sorted(dic.items(), key=lambda t: t[1]))   # 价格从低到高排序成有序字典


# 打印商品列表
def print_shop_dic(dic):
	for i, key in enumerate(dic, 1):
		print("%s. %-20s%10s" % (i, key, dic[key]))   # 打印出序号与物品名称及价格


# 生成一个选项与物品名称及价格对应的字典
def get_price_dict(dic):
	index_list = []
	content_list = []
	for i in range(1, len(dic) + 1):
		index_list.append(i)
	for j in dic.items():
		content_list.append(j)
	return dict(list(zip(index_list, content_list)))  # 字典格式：选项：(物品名称：价格)


# 结算
def check_out(general_budget, cart_list, ord_dic, remain_budget):
	print("正在结算，请稍后...")
	print("=" * 75)
	print("您的预算总额是：%60s" % general_budget)    # 打印用户最开始输入的预算
	print("-" * 75)
	print("购物清单：".center(75))
	print("-" * 75)
	shopping_cart_count = Counter(cart_list)   # Counter统计序列中元素出现的次数
	for key, val in shopping_cart_count.items():    # 打印出用户的购物清单
		print("商品名称：%-20s 数量：%-10s 单价：%8s 总价：%8s" % (
			key, shopping_cart_count[key], ord_dic[key], ord_dic[key] * shopping_cart_count[key]))
	print("-" * 75)
	print("您的余额：%66s" % remain_budget)
	print("=" * 75)
	print("谢谢惠顾！".center(75))


# 打印购物车
def print_shopping_cart(dic):
	shopping_cart_count = Counter(shopping_cart_list)
	for key, val in shopping_cart_count.items():
		print("商品名称：%-20s 数量：%-10s 单价：%8s 总价：%8s" % (
			key, shopping_cart_count[key], dic[key], dic[key] * shopping_cart_count[key]))
	print("-" * 75)


# 判断选择
def get_user_input(level):
	while True:
		if level == 1:  # 当调用处于购物商城界面时，有以下菜单
			user_choose = input("请输入您的选择，按P查看购物车，按Q结算退出：").strip()
			if user_choose.isdigit():
				user_choose = int(user_choose)
				return user_choose
			elif user_choose.upper() == 'Q':
				return 'Q'
			elif user_choose.upper() == 'P':
				return 'P'
			else:
				print("无效的输入，请重新输入！")
		elif level == 2:    # 当调用处于购物车界面时，有以下菜单
			user_choose = input("请输入您的选择，按B返回购物商城，按Q结算退出：").strip()
			if user_choose.upper() == 'B':
				return 'B'
			elif user_choose.upper() == 'Q':
				return 'Q'
			else:
				print("无效的输入，请重新输入！")
		else:   # 打印调用时的异常
			print("调用时出现参数错误！")


# 主函数
def main():
	checkout_flag = False   # 定义一个判断用户是否在购物车界面跳出的flag
	ordered_shop_dic = init_shop_dic(shop_dic)
	print_shop_dic(ordered_shop_dic)
	price_dict = get_price_dict(ordered_shop_dic)
	while not checkout_flag:    # 当用户的预算大于等于0时，就一直循环直到用户输入Q结算
		option = get_user_input(1)
		if option == 'P':
			print("正在打印购物车...")
			print("我的购物车".center(71, '*'))
			print_shopping_cart(ordered_shop_dic)
			while True:
				option2 = get_user_input(2)    # 获取用户在购物车界面的输入
				if option2 == 'B':  # 用户输入B则返回购物商城界面
					print_shop_dic(ordered_shop_dic)
					break
				elif option2 == 'Q':    # 用户在购物车界面输入Q则结算退出
					print("此处调用结算功能。。。")
					checkout_flag = True    # 用户在购物车界面结算时跳出主循环
					break   # 跳出购物车界面的循环
				else:
					print("无效的输入，请重新输入！")
		elif option == 'Q':    # 如果用户输入Q直接结算退出
			print("此处调用结算功能。。。")
			break
		else:
			if 0 < option <= len(ordered_shop_dic):   # 判断输入是否为有效数字
				object_name = price_dict[option][0]   # 定义物品名称
				shopping_cart_list.append(object_name)  # 将用户选择的物品名称加入购物车列表
				print("%s已加入购物车，按P查看购物车，按Q结算退出：" % price_dict[option][0])
			else:
				print("无效的输入，请重新输入！")


if __name__ == '__main__':
	main()
