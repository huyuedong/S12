from django.shortcuts import render, HttpResponse
from app01 import forms
from app01 import models

# Create your views here.


def special_case_2003(request):
	return HttpResponse("special_case_2003-->2003")


def year_archive(request, year):
	return HttpResponse("year_archive-->{}".format(year))


def month_archive(request, year, month):
	return HttpResponse("month_archive-->{}/{}".format(year, month))


def article_detail(request, year, month, article):
	return HttpResponse("article_detail-->{}/{}:{}".format(year, month, article))


def article_filetype_detail(request, year, month, article, filetype):
	return HttpResponse("article_filetype_detail-->{}/{}:{}.{}".format(year, month, article, filetype))


user_objs = [
	{"name": "alex", "age": "18"},
	{"name": "eric", "age": "19"},
	{"name": "rain", "age": "20"},
	{"name": "john", "age": "21"},
]


def payment_index(request, user):
	if request.method == "GET":
		return render(request, "app01/index.html", {"user_objs": user_objs})
	# return HttpResponse("welcome to payment index, {}... ".format(user))


def payment_by_cash(request, user):
	return HttpResponse("Hello tuhao:{}....".format(user))


def page1(request):
	return render(request, "app01/page1.html")


def page1_1(request):
	return render(request, "app01/page1_1.html")


def book_form(request):
	form = forms.BookForm(request.POST)
	if request.method == "POST":
		print(request.POST)
		if form.is_valid():
			print("form is ok!")
			print(form.cleaned_data)
			print(form.clean())
			form_data = form.cleaned_data
			form_data["publisher_id"] = request.POST.get("publisher_id")
			book_obj = models.Book(**form_data)
			book_obj.save()
		else:
			print(form.errors)
	
	publisher_list = models.Publisher.objects.all()
	return render(request, "app01/book_form.html", {"book_form": form, "publishers": publisher_list})


def book_model_form(request):
	form = forms.BookModelForm(request.POST)
	if request.method == "POST":
		print(request.POST)
		if form.is_valid():
			print("form is ok!")
			form.save()
	return render(request, "app01/book_model_form.html", {"book_form": form})