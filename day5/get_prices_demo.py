#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
获取购物车总价的Demo
"""

from collections import Counter


# 获取总价
def get_prices(cart_list, ord_dic):
	print("正在结算，请稍后...")
	print("购物清单：".center(75))
	shopping_cart_count = Counter(cart_list)   # Counter统计序列中元素出现的次数
	total_prices = 0
	for key, val in shopping_cart_count.items():    # 打印出用户的购物清单
		print("商品名称：%-20s 数量：%-10s 单价：%8s 总价：%8s" % (
			key, shopping_cart_count[key], ord_dic[key], ord_dic[key] * shopping_cart_count[key]))
		total_prices += ord_dic[key] * shopping_cart_count[key]
	return total_prices

l1 = ["a", "b", "c", "a", "a"]
d1 = {"a": 10, "b": 20, "c": 30}

a = get_prices(l1, d1)
print(a)
