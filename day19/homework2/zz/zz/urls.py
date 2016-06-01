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
from django.conf.urls import url, include
from django.contrib import admin
from cmdb import views
from crm import urls as crm_urls

urlpatterns = [
    url(r'^(?i)admin/', admin.site.urls),
    url(r'^(?i)login/$', views.acc_login),
    url(r'^(?i)logout/$', views.acc_logout),
    url(r'^(?i)signup/$', views.signup),
    url(r'^(?i)index/$', views.index),
    url(r'^(?i)ajax_add/$', views.ajax_add),
    url(r'^(?i)ajax_test/$', views.ajax_test),
    url(r'^(?i)test/$', views.test),
    url(r'^(?i)cmdb/', include("cmdb.urls")),
    url(r'^crm/', include(crm_urls)),
    url(r'.*', views.acc_login),
]
