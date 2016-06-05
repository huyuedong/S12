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
from django.conf.urls import url, include
from django.contrib import admin
from s12bbs import common_views
from bbs import urls as bbs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', common_views.acc_login, name="login"),
    url(r'^logout/', common_views.acc_logout, name="logout"),
    url(r'^signup/', common_views.signup, name="signup"),
    url(r'^bbs/', include(bbs_urls, namespace="bbs")),
    url(r'^.*', include(bbs_urls)),
]
