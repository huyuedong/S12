from django.shortcuts import render, HttpResponse, Http404, redirect
from cmdb.auth import auth
from django.apps import apps
from crm import models
from crm.forms import model_forms, get_modelform
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.


def get_obj(object_arg, str_arg):
	if hasattr(object_arg, str_arg):
		obj = getattr(object_arg, str_arg)
	else:
		obj = None
	return obj


def get_fields_list(obj):
	ret = []
	for field in obj._meta.get_fields():
		# if field.concrete:
		# 得到前端要显示的字段，默认不显示on_to_one和id
		if hasattr(field, "verbose_name") and not field.one_to_one and field.name != "id":
			ret.append(field)
	return ret


@auth.acc_auth
def index(request):
	user = request.session["NAME"]
	models_list = apps.get_app_config("crm").get_models()
	print(models_list)
	return render(request, "crm/index.html", {"models": models_list, "username": user})


@auth.acc_auth
def show(request, model_name_str):
	username = request.session["NAME"]
	model_name = get_obj(models, model_name_str)
	model_fields = get_fields_list(model_name)
	if model_name:
		query_set = model_name.objects.all()
		paginator = Paginator(query_set, 2)  # 分页显示记录，每页2条记录
		page = request.GET.get("page")
		try:
			ret = paginator.page(page)
		except PageNotAnInteger:
			ret = paginator.page(1)
		except EmptyPage:
			ret = paginator.page(paginator.num_pages)
		return render(
			request,
			"crm/show.html",
			{"query_set": ret, "model": model_name, "model_fields": model_fields, "username": username},
		)
	else:
		return Http404


# 添加记录
@auth.acc_auth
def add(request, model_name_str):
	global form_obj
	username = request.session["NAME"]  # 从session中获得登录的账号
	form_obj = get_modelform.get_modelform(model_name_str)
	model_name = get_obj(models, model_name_str)
	print(form_obj)
	if request.method == "POST":
		request_form = get_modelform.get_modelform(model_name_str, request.POST)  # 获取提交的form数据
		if request_form.is_valid():
			request_form.save()
			# request_data = request_form.clean()
			base_url = "/".join(request.path.split("/")[:-2])  # 截取保存成功后要跳转的url
			redirect_url = "{}/".format(base_url)
			return redirect(redirect_url)
		else:
			return render(
				request,
				"crm/add.html",
				{"username": username, "form_obj": request_form, "model": model_name},
			)
	return render(
			request,
			"crm/add.html",
			{"username": username, "form_obj": form_obj, "model": model_name},
	)


# 修改记录
@auth.acc_auth
def change(request, model_name_str, obj_id):
	username = request.session["NAME"]
	id_value = int(obj_id)  # 获得点击的记录ID
	model_name = get_obj(models, model_name_str)  # 得到该记录对应的model对象
	instance_obj = model_name.objects.get(id=id_value)  # 从数据中取到该记录的model实例

	modelform_obj = get_modelform.get_modelform(model_name_str, instance=instance_obj)  # 生成form对象
	if request.method == "POST":  # 提交
		print("=============>提交啦！")
		request_form = get_modelform.get_modelform(model_name_str, request.POST, instance=instance_obj)  # 得加实例
		if request_form.is_valid():
			print("验证成功！")
			request_form.save()
			# request_data = request_form.clean()
			# print(request_data)
			base_url = "/".join(request.path.split("/")[:-3])  # 截取保存成功后要跳转的url
			redirect_url = "{}/".format(base_url)
			return redirect(redirect_url)
		else:
			return render(
				request,
				"crm/add.html",
				{"username": username, "form_obj": request_form, "model": model_name},
			)
	return render(
			request,
			"crm/change.html",
			{"form_obj": modelform_obj, "model": model_name, "instance_name": str(instance_obj), "username": username},
	)


def url_name_test(request, word1, word2):
	return render(request, "crm/url_name_test.html")
