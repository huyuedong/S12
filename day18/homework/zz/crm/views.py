from django.shortcuts import render, HttpResponse
from cmdb.auth import auth
from django.apps import apps

# Create your views here.


@auth.acc_auth
def index(request):
	user = request.session["NAME"]
	models_list = apps.get_app_config("crm").get_models()
	print(models_list)
	return render(request, "crm/index.html", {"models": models_list, "username": user})


def show(request, model_name):
	print(model_name)
	return HttpResponse(model_name)

