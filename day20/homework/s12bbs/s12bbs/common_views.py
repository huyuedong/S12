#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: master@liwenzhou.com

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from s12bbs import login_signup_form
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

# Create your views here.


def acc_login(request):
	login_form_obj = login_signup_form.LoginForm()
	status = ""
	if request.method == "POST":
		login_form_obj = login_signup_form.LoginForm(request.POST)
		if login_form_obj.is_valid():
			user = authenticate(
				username=request.POST.get("username"),
				password=request.POST.get("password"),
			)
			if user is not None:
				login(request, user)
				return redirect(request.GET.get("next", "/bbs/"))
			else:
				status = "用户名或密码错误"

	return render(request, "common/login.html", {"login_form_obj": login_form_obj, "login_error": status})


def acc_logout(request):
	logout(request)
	return redirect("/bbs/")


def signup(request):
	signup_form_obj = login_signup_form.SignupForm()
	status = ""
	if request.method == "POST":
		signup_form_obj = login_signup_form.SignupForm(request.POST)
		logger.debug(signup_form_obj)
		if signup_form_obj.is_valid():
			signup_data = signup_form_obj.clean()
			if signup_data.get("password") == signup_data.get("repeat_password"):
				signup_data.pop("repeat_password")
				# 如何判断注册成功与失败？？？
				try:
					user = User.objects.create_user(**signup_data)
					# 如果没有错误信息就表明注册成功，跳转到登陆页面。
					if user:
						print("用户：{} 注册成功。".format(signup_data.get("username")))
						return redirect("/login/")
				except Exception as e:
					print(e)
					status = "注册失败。"
					if str(e).startswith("UNIQUE"):
						status = "用户名已存在"

			else:
				print("两次密码不一致")
				status = "两次密码不一致"
	return render(request, "common/signup.html", {"signup_form_obj": signup_form_obj, "status": status})

