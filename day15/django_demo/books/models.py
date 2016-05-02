from django.db import models

# Create your models here.


# 出版商
class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()

	def __str__(self):
		return self.name


# 作者
class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=40)
	email = models.EmailField()

	def __str__(self):
		return "{}{}".format(self.first_name, self.last_name)


# 书
class Book(models.Model):
	title = models.CharField(max_length=100)
	# 一本书可能有多个作者，一个作者可能写有多本书
	authors = models.ManyToManyField(Author)
	# 一本书默认只会有一个出版社
	publisher = models.ForeignKey(Publisher)
	publication_date = models.DateField()

	def __str__(self):
		return self.title

