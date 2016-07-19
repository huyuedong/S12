from django.conf.urls import url
from bbs import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(\d+)$', views.category,name='category'),
    url(r'^article/(\d+)$', views.article_detail,name='article'),
    url(r'^new_article/$', views.new_article,name='new_article'),
    url(r'^click_thumb/', views.click_thumb),
    url(r'^login/', views.acc_login, name='login'),
    url(r'^logout/', views.acc_logout, name='logout'),
    # url(r'^bbs/', include('bbs.urls')),
]