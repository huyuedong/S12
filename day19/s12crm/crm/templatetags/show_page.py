#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import template
from django.utils.html import format_html

register = template.Library()


# 直接把整个分页功能写成一个单独的simple_tag，方便复用
@register.simple_tag
def show_pages(obj, show_num):
	"""
	自定义的一个分页功能
	:param obj: paginator对象
	:param show_num: 当前页前后要显示的页码数
	:return:
	"""
	global previous_page_str
	global next_page_str
	show_pages_str = ''
	if obj.has_previous():  # 如果有上一页就显示左<<标志可点
		previous_page_str = '''
			<li class="">
				<a href="?page={}" aria-label="Previous">
					<span aria-hidden="true">&laquo;</span>
				</a>
			</li>'''.format(obj.previous_page_number())
	else:  # 没有上一页就给li标签添加一个disabled class，即显示<<不可点击
		previous_page_str = '''
			<li class="disabled">
				<a href="" aria-label="Previous">
					<span aria-hidden="true">&laquo;</span>
				</a>
			</li>'''
	for page in obj.paginator.page_range:  # 便利页码
		if abs(obj.number - page) < show_num:  # 如果在要显示的范围内
			if obj.number == page:  # 如果是当前页，就给当前的li标签添加一个active的class
				show_pages_str += '''
					<li class="active">
						<a href="?page={}">{}</a>
					</li>
					'''.format(page, page)
			else:  # 否则li标签就不加active
				show_pages_str += '''
					<li class="">
						<a href="?page={}">{}</a>
					</li>'''.format(page, page)
	if obj.has_next():  # 如果有下一页
		next_page_str = '''
			<li class="">
				<a href="?page={}" aria-label="Previous">
					<span aria-hidden="true">&raquo;</span>
				</a>
			</li>'''.format(obj.next_page_number())
	else:  # 没有下一页，就给li标签加一个disabled的class
		next_page_str = '''
			<li class="disabled">
				<a href="" aria-label="Previous">
					<span aria-hidden="true">&raquo;</span>
				</a>
			</li>'''
	html_str = "{}{}{}".format(previous_page_str, show_pages_str, next_page_str)  # 得到整个html字符串
	return format_html(html_str)  # 渲染返回给前端
