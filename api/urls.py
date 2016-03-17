__author__ = 'wanyama'
from django.conf.urls import patterns,include,url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('',
                       url(r'^donors/$',views.DonorList.as_view()),
                       url(r'^users/$',views.UserList.as_view()),
                       url(r'^donors/(?P<pk>[0-9]+)/$',views.DonorDetail.as_view()),
                       url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
)
