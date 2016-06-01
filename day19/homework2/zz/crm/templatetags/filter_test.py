#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import template

register = template.Library()


@register.filter
def value_upper(val):
	return val.upper()
