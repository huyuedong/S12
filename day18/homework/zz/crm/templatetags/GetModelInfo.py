#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

"""
获取model的verbose name
"""

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def get_verbose_name(object, field_name=None):
	if field_name:
		return object._meta.get_field(field_name).verbose_name.title()
	else:
		return object._meta.verbose_name


@register.simple_tag
def get_model_name(object):
		return object.__class__.__name__
