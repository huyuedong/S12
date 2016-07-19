from django.conf.urls import url,include
from django.contrib import admin
from bbs import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bbs/', include('bbs.urls')),
    url(r'^$', views.root)
]
