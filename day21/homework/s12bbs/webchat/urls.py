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
from webchat import views


urlpatterns = [
    url(r'^$', views.dashboard, name="chat_dashboard"),
    url(r'^msg_send/$', views.send_msg, name="send_msg"),
    url(r'^new_msgs/$', views.get_new_msgs, name="get_new_msgs"),
    url(r'^my_friends_status/$', views.check_my_friends_status, name="check_my_friends_status")

]

