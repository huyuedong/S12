from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from Sansa import core


# Create your views here.

@csrf_exempt
def asset_report(request):
	print(request.GET)
	if request.method == "POST":
		asset_handler = core.Asset(request)
		pass
