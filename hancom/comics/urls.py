"""
Comic URLs
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('hancom.comics.views',
    url(r'^(?P<comic_id>\d+)/$', 'comic_page', name='comic'),
)