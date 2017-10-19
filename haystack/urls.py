from django.conf.urls import patterns, url, include
from haystack.views import SearchView


urlpatterns = patterns('haystack.views',
    url(r'^$', SearchView(), name='haystack_search'),
)
