from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'africa_one.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('core.urls',namespace='core')),
    url(r'^manager/',include('admin.urls',namespace='admin')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^api-auth',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^api/',include('api.urls')),
    url(r'^rest-auth/',include('rest_auth.urls')),
) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



