"""s12day16 URL Configuration

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
from app01 import urls as payment_urls
from app01 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>[0-9]{4})$', views.year_archive),
    url(r'^articles/([0-9]{4})$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)$', views.article_detail),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+).(\w+)$', views.article_filetype_detail),
    # 给所有以payment开头的视图都传入了一个{"user": "alex"}参数
    # url(r'^payment/', include(payment_urls), {"user": "alex"}),
    url(r'^payment/', include(payment_urls)),

]
