from django.shortcuts import render, HttpResponse, redirect
from myadmin import models
import inspect
from myadmin.forms import change_book

# Create your views here.


# 找出模块里所有的类名
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
	if request.method == "POST":
		new_data = request.POST.dict()
		try:
			the_book = models.Book.objects.get(id=book_id)
			the_book.title = new_data.get("title")
			the_book.authors_id = new_data.get("authors")
			the_book.publisher_id = new_data.get("publisher")
			the_book.publication_date = new_data.get("publication_date")
			the_book.save()
		except Exception as e:
			print(e)
		return redirect("/myadmin/book/")
	else:
		# 根据url传过来的id找到那条数据
		book_data = models.Book.objects.get(id=book_id)
		# 找到书的作者们
		the_authors = book_data.authors.select_related()
		# 找到书的出版商
		the_publisher = book_data.publisher
		# 找出数据库中所有的作者
		all_authors = models.Author.objects.all()
		# 找出数据库中所有的出版商
		all_publishers = models.Publisher.objects.all()
		return render(
				request,
				"myadmin/book_change.html",
				{
					"i": book_data,
					"authors": all_authors,
					"publishers": all_publishers,
					"publisher_value": the_publisher,
					"authors_value": the_authors,
				}
		)


def publisher_change(request, publisher_id):
	if request.method == "POST":
		try:
			print(request.POST.dict())
			# 将修改的数据存入数据库
			models.Publisher.objects.create(**request.POST.dict())
			return redirect("/myadmin/publisher/")
		except Exception as e:
			print(e)
	else:
		# 根据id找到出版商
		publisher_data = models.Publisher.objects.get(id=publisher_id)

		return render(request, "myadmin/publisher_change.html", {"i": publisher_data})


def author_change(request, author_id):
	if request.method == "POST":
		try:
			print(request.POST.dict())
			# 将修改的数据存入数据库
			models.Author.objects.create(**request.POST.dict())
			return redirect("/myadmin/author/")
		except Exception as e:
			print(e)

	else:
		# 根据id找到作者
		author_data = models.Author.objects.get(id=author_id)

		return render(request, "myadmin/author_change.html", {"i": author_data})


# 添加书籍
def book_add(request):
	if request.method == "POST":
		try:
			models.Book.objects.create(**request.POST.dict())
		except Exception as e:
			print(e)
		return redirect("/myadmin/book/")
	else:
		# 找出数据库中所有的作者
		all_authors = models.Author.objects.all()
		# 找出数据库中所有的出版商
		all_publishers = models.Publisher.objects.all()
		return render(request, "myadmin/book_change.html", {"authors": all_authors, "publishers": all_publishers, "flag": "add"})


# 添加出版社
def publisher_add(request):
	if request.method == "POST":
		try:
			models.Publisher.objects.create(**request.POST.dict())
		except Exception as e:
			print(e)
		return redirect("/myadmin/publisher/")
	else:
		return render(request, "myadmin/publisher_change.html", {"flag": "add"})


# 添加作者
def author_add(request):
	if request.method == "POST":
		try:
			models.Author.objects.create(**request.POST.dict())
		except Exception as e:
			print(e)
		return redirect("/myadmin/author/")
	else:
		return render(request, "myadmin/author_change.html", {"flag": "add"})


# 删除
def delete(request, the_table_name, the_id):
	classes = get_classes(models)
	the_class_name = the_table_name.capitalize()
	if the_class_name in classes:
		# 反射获取到具体的models对象
		obj = getattr(models, the_class_name).objects.all().get(id=the_id)
		print(obj)
		for class_name in classes:
			if class_name != the_class_name:
				pass

		return render(request, "myadmin/delete.html", {"table_name": the_table_name, "obj": obj})
	else:
		print("err")
		return redirect(request, "/myadmin/{}/".format(the_table_name))
