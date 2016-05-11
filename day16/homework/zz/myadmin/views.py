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
	return render(request, "myadmin/index.html")


def book(request):
	books_data = models.Book.objects.all()
	return render(request, "myadmin/book.html", {"table_name": "book", "obj": books_data})


def publisher(request):
	publishers_data = models.Publisher.objects.all()
	return render(request, "myadmin/publisher.html", {"table_name": "publisher", "obj": publishers_data})


def author(request):
	authors_data = models.Author.objects.all()
	return render(request, "myadmin/author.html", {"table_name": "author", "obj": authors_data})
