from django.conf.urls import url
from . import views


urlpatterns = [
    url('post/$', views.post_list, name='post_list'),
    url('post/(?P<pk>\d+)/$', views.post_detail, name="post_detail"),
    url('post/new/$', views.post_new, name='post_new'),
    url('post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit')
]