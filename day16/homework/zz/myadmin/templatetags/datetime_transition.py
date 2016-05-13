#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
from django import template
from django.utils.safestring import mark_safe
from django.template.base import resolve_variable, Node, TemplateSyntaxError

register = template.Library()


@register.simple_tag
def datetime_2_str(arg):
	if arg:
		return arg.strftime("%Y-%m-%d")
	else:
		return ""
