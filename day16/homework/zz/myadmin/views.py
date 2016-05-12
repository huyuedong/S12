from django.shortcuts import render, HttpResponse
from myadmin import models
import inspect
from myadmin.forms import change_book

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


def book_change(request, book_id):
	book_data = models.Book.objects.get(id=book_id)
	the_authors = book_data.authors.select_related()
	the_publisher = book_data.publisher
	all_authors = models.Author.objects.all()
	all_publishers = models.Publisher.objects.all()
	print(the_authors, the_publisher)
	# r = models.Author.objects.all().order_by("id").values_list("id", "first_name", "last_name")
	# print(r)
	return render(request, "myadmin/book_change.html", {"i": book_data, "authors": all_authors, "publishers": all_publishers})
	# return HttpResponse("ok")


def publisher_change(request, publisher_id):
	return HttpResponse("OK")


def author_change(request, author_id):
	return HttpResponse("ok")
