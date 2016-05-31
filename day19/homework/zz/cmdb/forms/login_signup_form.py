#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				"type": "email",
				"class": "form-control",
				"placeholder": "邮箱",
			}
		),
		error_messages={
			"required": "邮箱不能为空",
		}
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"type": "password",
				"class": "form-control",
				"placeholder": "密码",
			}
		),
		error_messages={
			"required": "密码不能为空",
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
	email = forms.EmailField(
		widget=forms.TextInput(
			attrs={
				"type": "email",
				"class": "form-control",
				"placeholder": "请输入邮箱",
			}
		),
		error_messages={
			"required": "邮箱不能为空",
		}
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				"type": "password",
				"class": "form-control",
				"placeholder": "设置密码",
			}
		),
		error_messages={
			"required": "密码不能为空",
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
