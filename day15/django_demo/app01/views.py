from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse("This is the Home page!")


def index(request):
	return HttpResponse('This is app01.index')
