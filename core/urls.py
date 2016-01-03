from django.conf.urls import patterns,url
from core.views import *


urlpatterns = patterns('',
                       url(r'^$',index,name='home'),
                       url(r'^logout/',logout_view,name='logout'),
                       url(r'^sign_up/',sign_up,name='sign_up'),
                       url(r'^business_list',BusinessListView.as_view(),name='business_list'),
                       url(r'^business_add',BusinesView.as_view(),name='business_add'),
                       url(r'^business_edit/(?P<pk>\d+)/$',BusinesView.as_view(),name='business_edit'),
                       url(r'^add_business_successful',add_business_successful,name='add_business_successful'),
                       url(r'^review_list',ReviewListView.as_view(),name='review_list'),
                       url(r'^review_add/(?P<business_pk>\d+)/$',ReviewView.as_view(),name='review_add'),
                       url(r'^review_edit/(?P<pk>\d+)/$',ReviewView.as_view(),name='review_edit'),
                       )