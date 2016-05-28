from django.shortcuts import render
from crm import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def index(request):
	return render(request, "crm/dashboard.html")


def customers(request):
	customers_set = models.Customer.objects.all()
	# 生成分页实例
	paginator = Paginator(customers_set, 1)
	page = request.GET.get("page")
	try:
		customers_iter = paginator.page(page)
	# 如果获取的page不是数字，就默认返回第一页
	except PageNotAnInteger:
		customers_iter = paginator.page(1)
	# 如果获取的page不存在，就默认返回最后一页
	except EmptyPage:
		customers_iter = paginator.page(paginator.num_pages)

	return render(request, "crm/customers.html", {"customers": customers_iter})
