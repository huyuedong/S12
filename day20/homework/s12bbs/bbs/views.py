from django.shortcuts import render, redirect, HttpResponse
from bbs import models

# Create your views here.


# 从数据库中找出所有set_as_top_menu=True的版块，并按照position_index排序
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by("position_index")


# 首页
def index(request):
	category_obj = models.Category.objects.get(position_index=1)  # 找到第一个版块
	article_list = models.Article.objects.filter(status='published')  # 找到所有的发布的文章
	return render(request, 'bbs/index.html', {
		'category_list': category_list,
		'article_list': article_list,
		'category_obj': category_obj,
	})


# 版块页面
def category(request, category_id):
	category_obj = models.Category.objects.get(id=category_id)
	if category_obj.position_index == 1:  # 首页
		article_list = models.Article.objects.filter(status='published')
	else:
		article_list = models.Article.objects.filter(category_id=category_obj.id, status='published')
	return render(request, 'bbs/index.html', {
		'category_list': category_list,  # 顶部菜单
		'category_obj': category_obj,  # 版块对象
		'article_list': article_list,  # 文章列表
	})


# 文章页面
def article_detail(request, article_id):
	article_obj = models.Article.objects.get(id=article_id)
	return render(request, "bbs/article_detail.html", {
		"article_obj": article_obj,
		"category_list": category_list,
	})


# 评论提交
def post_comment(request):
	print(request.POST)
	print(request.user)
	if request.method == "POST":
		new_comment_obj = models.Comment(
			comment_type=request.POST.get("comment_type"),
			parent_comment_id=request.POST.get("parent_comment_id", None),
			article_id=request.POST.get("article_id"),
			user_id=request.user.userprofile.id,
			comment=request.POST.get("comment"),
		)
		new_comment_obj.save()
	return HttpResponse("OK")
