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
from crm import views

urlpatterns = [
    url(r'^$', views.index, name="crm_index"),
    url(r'^(?P<model_name_str>\w+)/$', views.show, name="model_detail"),
    url(r'^(?P<model_name_str>\w+)/add/$', views.add, name="add_model_detail"),
    url(r'^(?P<model_name_str>\w+)/(?P<obj_id>\d+)/change/$', views.change, name="change_model_detail"),
    url(r'^(?P<word1>\w+)/(?P<word2>\w+)/from/Q1mi/$', views.url_name_test, name="url_name_test"),

]
