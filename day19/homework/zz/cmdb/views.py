from django.shortcuts import render, redirect, HttpResponse
from cmdb.forms import login_signup_form
from cmdb.forms import add_record
from cmdb import models
import logging
from cmdb.auth import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

import json

logger = logging.getLogger(__name__)


# 登录
def acc_login(request):
	obj = login_signup_form.LoginForm()

	if request.method != "POST":
		return render(request, "cmdb/login.html", {"obj": obj})
	# 把提交到的所有数据封装到LoginForm()
	user_input_obj = login_signup_form.LoginForm(request.POST)
	if not user_input_obj.is_valid():
		error_msg = user_input_obj.errors.as_data()
		return render(request, "cmdb/login.html", {"obj": user_input_obj, "errors": error_msg})
	login_data = user_input_obj.clean()
	username = login_data.get("username", "")
	password = login_data.get("password", "")
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			request.session["IS_LOGIN"] = 1
			request.session["NAME"] = user.username
			request.session.set_expiry(0)
			return redirect("/index/")
	else:
		return render(request, "cmdb/login.html", {"obj": user_input_obj, "status": "用户名或密码错误"})


# 注销
def acc_logout(request):
	del request.session["IS_LOGIN"]
	logout(request)
	return redirect("/login/")


def signup(request):
	obj = login_signup_form.SignupForm()
	if request.method == "POST":
		signup_obj = login_signup_form.SignupForm(request.POST)
		logger.debug(signup_obj)
		if signup_obj.is_valid():
			signup_data = signup_obj.clean()
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
					return render(request, "cmdb/signup.html", {"obj": signup_obj, "status": e})

			else:
				print("两次密码不一致")
				sign_status = "两次密码不一致"
				return render(request, "cmdb/signup.html", {"obj": signup_obj, "status": sign_status})
		else:
			error_msg = signup_obj.errors.as_data()
			return render(request, "cmdb/signup.html", {"obj": signup_obj, "errors": error_msg})
	return render(request, "cmdb/signup.html", {"obj": obj})


@auth.acc_auth
def index(request):
	host_data = models.HostInfo.objects.all()
	user = request.session["NAME"]
	return render(request, "cmdb/index.html", {"username": user, "obj": host_data})


@auth.acc_auth
def add(request):
	if request.method == "POST":
		input_record_obj = add_record.AddRecordForm(request.POST)
		return render(request, "cmdb/add_record.html", {"obj": input_record_obj})
	obj = add_record.AddRecordForm()
	return render(request, "cmdb/add_record.html", {"obj": obj})


@auth.acc_auth
def ajax_add(request):
	ret = {"status": True, "errors": ""}
	try:
		print(request.POST)
		request_dic = dict(request.POST)
		add_data_dic = {}
		for key in request_dic:
			add_data_dic[key] = request_dic[key][0]
		models.HostInfo.objects.create(**add_data_dic)
	except Exception as e:
		ret["status"] = False
		ret["errors"] = str(e)
	finally:
		return HttpResponse(json.dumps(ret))


@auth.acc_auth
def ajax_req(request):
	ret = {"status": True, "errors": ""}
	try:
		# print(request.POST)
		# request_dic = json.loads(request.POST.data_list)
		request_dic = dict(request.POST)
		# print(request_dic)
		request_list = request_dic["data_list"]
		# print(request_list[0])
		modify_data = json.loads(request_list[0])
		# print(modify_data)
		operate_list = []
		for i in modify_data:
			id = i["id"]
			i.pop("id")
			# 此处转换得到一个< 数据的id:数据内容 >的格式
			temp_dic = {id: i}
			operate_list.append(temp_dic)
		print(operate_list)
		# 遍历要操作的记录列表,j是每一条需要操作的数据
		for j in operate_list:
			# key是每条要更新的数据的id值
			for key in j:
				# 根据id找到记录，然后更新
				models.HostInfo.objects.filter(id=key).update(**j[key])
	except Exception as e:
		ret["status"] = False
		ret["errors"] = str(e)
	finally:
		return HttpResponse(json.dumps(ret))


def test(request):
	return render(request, "cmdb/ajax_test.html")


def ajax_test(request):
	print(request.POST)
	return HttpResponse("OK")
