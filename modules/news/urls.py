from django.conf.urls import patterns, url

urlpatterns = patterns('news.views',
    url(r'^$', 'accueil'),
   	url(r'^/list/article/(?P<id>\d+)-(?P<slug>.+)$', 'lire'),
)