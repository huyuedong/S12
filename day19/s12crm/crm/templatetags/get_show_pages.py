#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import template
from django.utils.html import format_html

register = template.Library()


@register.filter
def value_upper(val):
	return val.upper()


# 获得需要展示的页码数
@register.simple_tag
def get_show_pages(current_page, loop_num):
	offset = abs(current_page - loop_num)
	# 只显示当前页前后三页的页码数
	if offset < 3:
		if current_page == loop_num:
			page_str = '<li class="active"><a href="?page={}">{}</a></li>'.format(loop_num, loop_num)
		else:
			page_str = '<li class=""><a href="?page={}">{}</a></li>'.format(loop_num, loop_num)
		return format_html(page_str)
	else:
		return ""

