#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import forms


class ArticleForm(forms.Form):
	title = forms.CharField(min_length=5, max_length=255)
	brief = forms.CharField(min_length=5, max_length=255)
	category_id = forms.IntegerField()
	head_img = forms.ImageField()
	content = forms.CharField(min_length=10)

