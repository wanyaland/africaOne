from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'africa_one.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('core.urls',namespace='core')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^review',include('review.urls')),
) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


