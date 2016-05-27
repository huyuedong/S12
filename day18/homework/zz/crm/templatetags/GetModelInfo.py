#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
获取model的verbose name
"""

from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def get_verbose_name(obj, field_name=None):
	if field_name:
		return obj._meta.get_field(field_name).verbose_name.title()
	else:
		return obj._meta.verbose_name


@register.simple_tag
def get_model_name(obj):
		return obj.__class__.__name__


@register.simple_tag
def get_fields(obj):
	global field_data
	html_td = ""
	fields_list = obj._meta.fields
	for field in fields_list:
		print(field.name)
		if field.many_to_many:  # 如果是多对多
			field_area = field.select_related()
			area_data = []
			for area in field_area:
				area_data.append(str(area))
			field_data = ",".join(area_data)
		if field.choices:  # 如果是选项
			field_str = getattr(obj, "get_{}_display".format(field.name))
			field_data = field_str()
		else:  # 其他就直接显示
			field_data = getattr(obj, field.name)
			# try:
			# 	field_data = getattr(obj, field.name)
			# except AttributeError:
			# 	continue
		html_td += "<td name='{}'>{}</td>".format(field.name, field_data)
	return format_html(html_td)

