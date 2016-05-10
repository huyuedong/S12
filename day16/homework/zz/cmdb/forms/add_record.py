#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django import forms
from django.core.exceptions import ValidationError
import re
from cmdb import models


def port_validate(value):
	if not (value.isdigit() and int(value) < 65536):
		raise ValidationError("端口号格式错误")


class AddRecordForm(forms.Form):
	HOST_STATE_TYPE = (
		(1, "在线"),
		(2, "下线"),
	)
	HOST_GROUP_TYPE = (
		(1, "研发"),
		(2, "测试"),
		(3, "运维"),
	)
	SERVICE_TYPE = (
		(1, "tomcat"),
		(2, "MySQL"),
		(3, "Nginx"),
		(4, "FTP"),
	)
	hostname = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"type": "hostname",
				"class": "form-control",
				"placeholder": "主机名",
			}
		),
		error_messages={
			"required": "主机名不能为空",
		}
	)
	ip = forms.GenericIPAddressField(
		widget=forms.TextInput(
			attrs={
				"type": "ip",
				"class": "form-control",
				"placeholder": "ip地址",
			}
		),
		error_messages={
			"required": "ip地址不能为空",
		}
	)
	port = forms.CharField(
		widget=forms.TextInput(
			attrs={
				"type": "port",
				"class": "form-control",
				"placeholder": "端口",
			}
		),
		validators=[port_validate, ],
		error_messages={
			"required": "端口不能为空",
		}
	)
	service = forms.IntegerField(
		widget=forms.Select(
			choices=SERVICE_TYPE,
			attrs={
				"type": "service",
				"class": "form-control",
				"placeholder": "服务",
			}
		),
		error_messages={
			"required": "服务不能为空",
		}
	)
	group = forms.IntegerField(
		widget=forms.Select(
			choices=HOST_GROUP_TYPE,
			attrs={
				"type": "group",
				"class": "form-control",
				"placeholder": "业务组",
			}
		),
		error_messages={
			"required": "业务组不能为空",
		}
	)
	state = forms.IntegerField(

		widget=forms.Select(
			choices=HOST_STATE_TYPE,
			attrs={
				"type": "state",
				"class": "form-control",
				"placeholder": "状态",
			}
		),
		error_messages={
			"required": "状态不能为空",
		}
	)

	def __init__(self, *args, **kwargs):
		super(AddRecordForm, self).__init__(*args, **kwargs)
		self.fields['group'].widget.choices = models.HostGroup.objects.all().order_by('id').values_list('id', 'group_name')
		# self.fields['state'].widget.choices = models.HostInfo.objects.all().order_by('id').values_list('id', 'name')
