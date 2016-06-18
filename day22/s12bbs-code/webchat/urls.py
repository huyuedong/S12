
from django.conf.urls import url,include
from webchat import views
urlpatterns = [

    url(r'^$', views.dashboard,name='chat_dashboard'),
    url(r'^msg_send/$', views.send_msg,name='send_msg'),
    url(r'^new_msgs/$', views.get_new_msgs,name='get_new_msgs'),
    url(r'^fileUpload/$', views.upload_file, name="upload_file"),
    url(r'^upload_file_progress/$', views.upload_file_progress, name="upload_file_progress"),
    url(r'^delete_cache_key/$', views.delete_cache_key, name="delete_cache_key"),

]
