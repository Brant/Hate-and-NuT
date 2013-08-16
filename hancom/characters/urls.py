"""
URL configurations for sposorships
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('hancom.characters.views',
    url(r'^$', 'character_index', name='characters_index'),
)
