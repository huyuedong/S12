#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
"""
form 表单
"""
from django import forms
from app01 import models


class BookForm(forms.Form):
	title = forms.CharField(max_length=10)
	publication_Date = forms.DateField()


class BookModelForm(forms.ModelForm):
	class Meta:
		model = models.Book
		exclude = ()
		widgets = {
			"title": forms.TextInput(attrs={"class": "form-control"}),
		}
