from django.conf.urls import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'list_modules'),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)$', 'list_projects'),
    url(r'^(?P<slug_module>[-A-Za-z0-9_]+)/(?P<slug_project>[-A-Za-z0-9_]+)$', 'view_project'),
    url(r'^(?P<type>\d+)/(?P<slug>[-A-Za-z0-9_]+)$', 'module'),
)