#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com
from django.forms import ModelForm
from crm import models


def get_obj(object_arg, str_arg):
	if hasattr(object_arg, str_arg):
		obj = getattr(object_arg, str_arg)
	else:
		obj = None
	return obj


def get_modelform(model_str, *args, **kwargs):
	class MyForm(ModelForm):
		class Meta:
			model_obj = get_obj(models, model_str)
			model = model_obj
			fields = "__all__"

		def __init__(self, *args, **kwargs):
			super(MyForm, self).__init__(*args, **kwargs)
			for field_name in self.base_fields:
				field = self.base_fields[field_name]
				field.widget.attrs.update({"class": "form-control"})
	return MyForm(*args, **kwargs)
