__author__ = 'pedro'

from django.conf.urls import patterns, url

from StudentHelp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<palabra>\d+)/$', views.word, name='word')
)