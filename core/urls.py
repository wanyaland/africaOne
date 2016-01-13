from django.conf.urls import patterns,url
from core.views import *
from djangoratings.views import AddRatingFromModel


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
                       url(r'^business-user-edit/(?P<pk>\d+)/$',BusinessUserView.as_view(),name='business_user_edit'),
                       url(r'business-user-add',BusinessUserView.as_view(),name='business_user_add'),
                       url(r'business-detail/(?P<pk>\d+)/$',BusinessDetail.as_view(),name='business_detail'),
                       url(r'add-photo/(?P<pk>\d+)/$',add_photo,name='add_photo'),
                       url(r'sort-review/(?P<pk>\d+)/(?P<sort_by>\w+)/$',sort_review,name='sort_review'),
                       url(r'user-detail/(?P<pk>\d+)/$',UserDetail.as_view(),name='user_detail'),
                       url(r'user-list',UserList.as_view(),name='user_list'),
                       url(r'sign-up-business-results',ClaimBusinessList.as_view(),name='sign_up_business_results'),
                       )