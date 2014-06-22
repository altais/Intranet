from django.conf.urls import patterns, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'list_modules'),
    url(r'^(?P<slug>[-A-Za-z0-9_]+)$', 'list_projects', name='list_projects'),
    url(r'^inscription/(?P<type>[-A-Za-z0-9_]+)/(?P<slug>[-A-Za-z0-9_]+)$', 'inscription', name='inscription'),
    url(r'^(?P<slug_module>[-A-Za-z0-9_]+)/(?P<slug_project>[-A-Za-z0-9_]+)$', 'view_project', name='view_project'),


)