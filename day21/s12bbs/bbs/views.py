#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

from bbs import models

# 从数据库中找出所有set_as_top_menu=True的版块，并按照position_index排序
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by("position_index")


def index(request):
	# 找到第一个版块
	category_obj = models.Category.objects.get(position_index=1)
	# 找到所有的发布的文章
	article_list = models.Article.objects.filter(status='published')
	return render(request, 'bbs/index.html', {
		'category_list': category_list,
		'article_list': article_list,
		'category_obj': category_obj,
	})


def category(request, category_id):
	category_obj = models.Category.objects.get(id=category_id)
	if category_obj.position_index == 1:  # 首页
		article_list = models.Article.objects.filter(status='published')
	else:
		article_list = models.Article.objects.filter(category_id = category_obj.id,status='published')
	return render(request, 'bbs/index.html', {
		'category_list': category_list,
		'category_obj': category_obj,
		'article_list': article_list,
	})


def acc_login(request):
	if request.method == "POST":
		print(request.POST.get("username"))
		print(request.POST.get("password"))
		user = authenticate(
			username=request.POST.get("username"),
			password=request.POST.get("password"),
		)
		if user is not None:
			login(request, user)
			return redirect(request.GET.get("next", "/bbs/"))
		else:
			login_error = "用户名或密码错误"
			return render(request, 'login.html', {'login_err': login_error})
	return render(request, 'login.html')


def article_detail(request, article_id):
	article_obj = models.Article.objects.get(id=article_id)
	return render(
		request,
		"bbs/article_detail.html",
		{
			"article_obj": article_obj,
			"category_list": category_list,
		}
	)


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


def acc_logout(request):
	logout(request)
	return redirect("/bbs/")
