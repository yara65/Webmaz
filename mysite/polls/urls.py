

#! /usr/bin/env python 

from django.conf.urls import patterns,include, url
from django.contrib import admin
from polls.views import PostsListView, PostDetailView 

from .import views

urlpatterns = [
     # ex: /polls/
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]



urlpatterns = patterns('',
url(r'^$', PostsListView.as_view(), name='list'), 
                                               
url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()), 
                                              

)