from django.shortcuts import render, HttpResponse
from cmdb.auth import auth
from django.apps import apps
from crm import models
from crm.forms import model_forms

# Create your views here.


@auth.acc_auth
def index(request):
	user = request.session["NAME"]
	models_list = apps.get_app_config("crm").get_models()
	print(models_list)
	return render(request, "crm/index.html", {"models": models_list, "username": user})


def show(request, model_name):
	form_str = "{}Form".format(model_name)
	if hasattr(model_forms, form_str):
		form_name = getattr(model_forms, form_str)
		form_obj = form_name()
		return render(request, "crm/show.html", {"name": model_name, "obj": form_obj})
	else:
		return HttpResponse(model_name)

