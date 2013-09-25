"""
Comic URLs
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('hancom.comics.views',
    url(r'^random/$', 'random_comic_url', name='comic_random_url'),
    url(r'^(?P<comic_id>\d+)/$', 'comic_page', name='comic'),
    url(r'^archive/$', 'archive_index', name='archive_index'),
    url(r'^story/(?P<arc_slug>[\w\-]+)/$', 'storyarc_redirect', name='comic_story_redirect'),

)
