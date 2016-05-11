from django.shortcuts import render
from myadmin import models
import inspect

# Create your views here.


def get_classes(arg):
	classes = []
	clsmembers = inspect.getmembers(arg, inspect.isclass)
	for (name, _) in clsmembers:
		classes.append(name)
	return classes


def index(request):
	table_list = get_classes(models)
	print(table_list)
	return render(request, "master/myadmin/myadmin_master.html")
