from django.shortcuts import render, HttpResponse
from cmdb.auth import auth
from django.apps import apps
from crm import models
from crm.forms import model_forms

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
		if hasattr(field, "verbose_name") and not field.one_to_one:
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
		return render(request, "crm/show.html", {"query_set": query_set, "model": model_name, "model_fields": model_fields, "username": username})
	else:
		return HttpResponse("views.show ERROR")


@auth.acc_auth
def add(request, model_name_str):
	global form_obj
	username = request.session["NAME"]
	form_str = "{}Form".format(model_name_str)
	model_name = get_obj(models, model_name_str)
	print(model_name)
	form_name = get_obj(model_forms, form_str)
	if request.method == "POST":
		request_form = form_name(request.POST)
		if request_form.is_valid():
			request_form.save()
			request_data = request_form.clean()
			print(request_data)
			return HttpResponse("OK")
	else:
		if model_name and form_name:
			form_obj = form_name()
	return render(request, "crm/add.html", {"username": username, "form": form_obj, "model": model_name})


@auth.acc_auth
def change(request, model_name_str, id_value):
	id_value = int(id_value)
	model_name = get_obj(models, model_name_str)
	model_obj = model_name.objects.get(id=id_value)
	form_name_str = "{}Form"
	form_name = get_obj(model_forms, form_name_str)
	if model_name and form_name:
		form_obj = form_name(model_obj)
		return render(request, "crm/change.html", {"obj": form_obj})
	else:
		return HttpResponse("views.change ERROR")
