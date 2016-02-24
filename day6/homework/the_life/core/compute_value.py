#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"

"""
操作属性值
"""

from conf import setting


def compute_value(player_object, action_type, amounts, **others):
	"""
	所有操作属性值的行为都使用这个来计算
	:param player_object: 玩家实例
	:param action_type: 行为类型
	:param amounts: 数量
	:param others: 其他
	:return:
	"""
	amounts = int(amounts)
	if action_type in setting.ACTION_TYPE:
		attr = setting.ACTION_TYPE[action_type].get("attr")
		change_value = setting.ACTION_TYPE[action_type].get("per_value") * amounts
		operator = setting.ACTION_TYPE[action_type].get("operator")
		try:
			value = int(player_object.get_attr("confidence"))
			if operator == "plus":
				value += change_value
			elif operator == "minus":
				value -= change_value
			player_object.set_attr(attr, value)
			return player_object
		except ValueError:
			return None

	else:
		print("行为类型不存在！")
