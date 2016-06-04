"""s12bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bbs import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^category/(?P<category_id>\d+)/$', views.category),
    url(r'^article_detail/(?P<article_id>\d+)/$', views.article_detail, name="article_detail"),
    url(r'^post_comment/$', views.post_comment, name="post_comment"),
]
