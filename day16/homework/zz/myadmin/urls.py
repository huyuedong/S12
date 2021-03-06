"""zz URL Configuration

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
from myadmin import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'book/$', views.book),
    url(r'book/add/$', views.book_add),
    url(r'book/(?P<book_id>\d+)/change/$', views.book_change),
    url(r'publisher/$', views.publisher),
    url(r'publisher/add/$', views.publisher_add),
    url(r'publisher/(?P<publisher_id>\d+)/change/$', views.publisher_change),
    url(r'author/$', views.author),
    url(r'author/add/$', views.author_add),
    url(r'author/(?P<author_id>\d+)/change/$', views.author_change),
    url(r'(?P<the_table_name>\w+)/(?P<the_id>\d+)/delete/$', views.delete),
]
