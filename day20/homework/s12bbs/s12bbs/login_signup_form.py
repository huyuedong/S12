#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
	username = forms.CharField(
		label="username",
		max_length=26,
		widget=forms.TextInput(
			attrs={
				"type": "username",
				"class": "form-control",
				"placeholder": "用户名",
				"autofocus": "",
			}
		),
		error_messages={
			"required": "用户名不能为空",
			"max_length": "用户名过长",
		}
	)
	password = forms.CharField(
		min_length=8,
		widget=forms.PasswordInput(
			attrs={
				"type": "password",
				"class": "form-control",
				"placeholder": "密码",
			}
		),
		error_messages={
			"required": "密码不能为空",
			"min_length": "密码长度需大于8"
		}
	)
	remember_me = forms.CharField(
		widget=forms.CheckboxInput(
			attrs={
				"type": "checkbox",
			}
		)
	)


def repeat_validate():
	pass


class SignupForm(forms.Form):
	username = forms.CharField(
		label="username",
		max_length=25,
		min_length=4,
		widget=forms.TextInput(
			attrs={
				"type": "username",
				"class": "form-control",
				"placeholder": "请输入用户名",
			}
		),
		error_messages={
			"required": "用户名不能为空",
			"max_length": "同户名长度不能超过26",
			"min_length": "同户名长度不能小于4",
		}
	)
	password = forms.CharField(
		label="password",
		min_length=8,
		widget=forms.PasswordInput(
			attrs={
				"type": "password",
				"class": "form-control",
				"placeholder": "设置密码",
			}
		),
		error_messages={
			"required": "密码不能为空",
			"min_length": "密码长度不能小于8",
		}
	)
	repeat_password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"type": "password",
				"class": "form-control",
				"placeholder": "确认密码",
			}
		),
		error_messages={
			"required": "确认密码不能为空",

		}
	)
