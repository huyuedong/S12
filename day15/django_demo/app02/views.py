from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import ValidationError
from django import forms
import re
import json


# Create your views here.


def mobile_validate(value):
	mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
	if not mobile_re.match(value):
		raise ValidationError("手机号码格式错误")


class UserInfo(forms.Form):
	user_type_choice = (
		(0, "普通用户"),
		(1, "高级用户"),
	)
	user_type = forms.IntegerField(
		widget=forms.widgets.Select(
			choices=user_type_choice,
			attrs={"class": "form-control"}
		)
	)
	email = forms.EmailField(
		required=True,
		error_messages={"required": "邮箱不能为空"},
	)
	host = forms.CharField(error_messages={"required": "主机不能为空"},)
	port = forms.CharField(error_messages={"required": "端口不能为空"},)
	mobile = forms.CharField(
		validators=[mobile_validate, ],
		error_messages={
			"required": "手机不能为空"
		},
		widget=forms.TextInput(attrs={
			"class": "form-control",
			"placeholder": "手机号码",
		},
		)
	)
	memo = forms.CharField(
		required=False,
		widget=forms.Textarea(attrs={
			"class": "",
			"placeholder": "备注",
		})
	)


def index(request):
	return HttpResponse('This is app02.index')


def user_list(request):
	obj = UserInfo()
	if request.method == "POST":
		# 不明白
		user_input_obj = UserInfo(request.POST)
		# print(user_input_obj.is_valid())
		if user_input_obj.is_valid():
			data = user_input_obj.clean()
			print(data)
		else:
			error_msg = user_input_obj.errors.as_data()
			return render(request, "user_list.html", {"obj": user_input_obj, "errors": error_msg})
	return render(request, "user_list.html", {"obj": obj})


def ajax_demo(request):
	print(request.POST)
	return HttpResponse("ok")


def ajax_demo_set(request):
	ret = {"status": True, "error": ""}
	try:
		print(request.POST)
	except Exception as e:
		ret["status"] = False
		ret["error"] = str(e)
	return HttpResponse(json.dumps(ret))
