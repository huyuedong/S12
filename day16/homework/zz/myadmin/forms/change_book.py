#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import forms
from django.core.exceptions import ValidationError
from myadmin import models


class BookFrom(forms.Form):
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"type": "hostname",
				"class": "form-control",
				"placeholder": "",
			}
		),
		error_messages={
			"required": "主机名不能为空",
		}
	)
	authors = forms.IntegerField(
		widget=forms.SelectMultiple(
		),
		error_messages={
			"required": "作者不能为空",
		}
	)
	publisher = forms.IntegerField(
		widget=forms.Select(

		),
		error_messages={
			"required": "出版社不能为空",
		}
	)
	publication = forms.DateField(
		widget=forms.SelectDateWidget(

		),
		error_messages={
			"required": "出版日期不能为空",
		}
	)

	def __init__(self, *args, **kwargs):
		super(BookFrom, self).__init__(*args, **kwargs)
		self.fields["authors"].widget.choices = models.Author.objects.all().order_by("id").values_list("id")
		self.fields["publisher"].widget.choices = models.Author.objects.all().order_by("id").values_list("id")

