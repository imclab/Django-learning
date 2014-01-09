from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Finnish.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^word/', include('StudentHelp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
