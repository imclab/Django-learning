__author__ = 'pedro'

from django.conf.urls import patterns, url

from StudentHelp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^quiz/$', views.quiz, name='quiz'),
                       url(r'^search_form/$', views.search_form, name='search_form'),
                       url(r'^display_meta/$', views.display_meta, name='display_meta'),
                       url(r'^search/$', views.search, name='search'),
                       url(r'^(?P<palabra>\d+)/$', views.word, name='word'),
)