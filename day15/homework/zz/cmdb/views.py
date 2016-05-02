from django.shortcuts import render, redirect, HttpResponse
from cmdb.forms import login_signup_form
from cmdb.forms import add_record
from cmdb import models


# Create your views here.

import hashlib


# 预设一个加密算法
def md5_encryption(arg):
	try:
		# 将传入的参数按utf-8编码
		m = arg.encode("utf-8")
		# 创建添加自定义key的md5对象
		h = hashlib.md5("alex".encode("utf-8"))
		# 生成加密串
		h.update(m)
		# 返回十六进制的加密串
		return h.hexdigest()
	except TypeError:
		return None


def login(request):
	obj = login_signup_form.LoginForm()

	if request.method == "POST":
		# 把提交到的所有数据封装到LoginForm()
		user_input_obj = login_signup_form.LoginForm(request.POST)
		if user_input_obj.is_valid():
			login_data = user_input_obj.clean()
			print(models.UserInfo.objects.filter(email=login_data.get("email")))
			# TODO 怎么根据email查到密码
			# if models.UserInfo.objects.filter(email=login_data.get("email")).password == md5_encryption(login_data.get("password", "")):
			# 	request.session["is_login"] = "true"
			return redirect("/index/")

		else:
			error_msg = user_input_obj.errors.as_data()
			# print(error_msg)
			return render(request, "login.html", {"obj": user_input_obj, "errors": error_msg})
	return render(request, "login.html", {"obj": obj})


def signup(request):
	obj = login_signup_form.SignupForm()
	if request.method == "POST":
		signup_obj = login_signup_form.SignupForm(request.POST)
		if signup_obj.is_valid():
			signup_data = signup_obj.clean()
			if signup_data.get("password") == signup_data.get("repeat_password"):
				signup_data.pop("repeat_password")
				signup_data["password"] = md5_encryption(signup_data.get("password"))
				models.UserInfo.objects.create(**signup_data)

			else:
				print("两次密码不一致")
		else:
			error_msg = signup_obj.errors.as_data()
			return render(request, "signup.html", {"obj": signup_obj, "errors": error_msg})
	return render(request, "signup.html", {"obj": obj})


def index(request):
	return render(request, "index.html")


def add(request):
	if request.method == "POST":
		input_record_obj = add_record.AddRecordForm(request.POST)
		return render(request, "add_record.html", {"obj": input_record_obj})
	obj = add_record.AddRecordForm()
	return render(request, "add_record.html", {"obj": obj})
