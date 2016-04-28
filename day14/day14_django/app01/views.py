# coding:utf-8
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django import forms

# Create your views here.


def hello(request):
	return HttpResponse("hello world!")


class UserInfo(forms.Form):
	email = forms.EmailField(
		widget=forms.TextInput(attrs={
			"type": "email",
			"class": "form-control",
			"placeholder": "请输入邮箱",
		}),
		error_messages={
			"required": "邮箱不能为空",
		}
	)
	repeatpassword = forms.PasswordInput()


def login(request):
	# 如果是get请求，直接返回
	# 如果是POST，进行验证
	if request.method == "GET":
		return render(request, "login.html")
	if request.method == "POST":
		input_email = request.POST["email"]
		input_password = request.POST["password"]
		if input_email == "alex@alex.com" and input_password == "1234":
			from django.shortcuts import redirect
			return redirect("/index/")
		else:
			return render(request, "login.html", {"status": "用户名或密码错误。"})


def signup(request):
	# obj = UserInfo()
	if request.method == "POST":
		pass
		# user_input_obj = UserInfo(request.POST)
		# if user_input_obj.is_valid():
		# 	user_input_obj.clean()
		# else:
		# 	error_msg = user_input_obj.errors
		# 	return render(request, "signup.html", {"obj": obj, "errors": error_msg})
	if request.method == "GET":
		return render(request, "signup.html")


def index(request):
	return render(request, "index.html")
