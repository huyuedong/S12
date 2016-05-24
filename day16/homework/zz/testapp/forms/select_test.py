#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import forms


class SelectTestForm(forms.Form):
	city = forms.IntegerField(
		widget=forms.Select(
			choices=(
				(1, "BeiJing"),
				(2, "WeiHai"),
				(3, "RuShan"),
			),
			attrs={
				"class": "form-control",
			}
		),
		required=True
	)

	modes = forms.TypedChoiceField(
		coerce=lambda x: x == "1",
		choices=(
			(1, "负载均衡"),
			(2, "极致性能"),
			(3, "超级无敌"),
		),
		widget=forms.CheckboxSelectMultiple(

		),
	)

	def __init__(self, *args, **kwargs):
		super(SelectTestForm, self).__init__(*args, **kwargs)
		# self.fields["modes"].widget._empty_value = [2, ]  # 方法1
		self.initial["modes"] = [2, ]  # 方法2
		self.initial["city"] = 2















		self.initial["city"] = 2
