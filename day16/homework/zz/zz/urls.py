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
from cmdb import urls as cmdb_urls
from myadmin import urls as myadmin_urls
from testapp import urls as test_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', views.login),
    url(r'^signup/$', views.signup),
    url(r'^index/$', views.index),
    url(r'^ajax_add/$', views.ajax_add),
    url(r'^cmdb/', include(cmdb_urls)),
    url(r'^myadmin/', include(myadmin_urls)),
    url(r'^test/', include(test_urls))
    # url(r'.*', views.login),
]
