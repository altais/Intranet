#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView 

urlpatterns = patterns('forum.views',
    url(r"^forum/(\d+)/$", "forum"),
    url(r"^topic/(\d+)/$", "topic"),
    url(r"^new_post/$", "new_post"),
    url(r"^create_topic/$", "create_topic"),
    url(r'^new_topic/$',TemplateView.as_view(template_name="forum/new_topic.html")),
    url(r"^$", "main"),
)