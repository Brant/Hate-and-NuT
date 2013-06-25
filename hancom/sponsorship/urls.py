"""
URL configurations for sposorships
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('hancom.sponsorship.views',
    url(r'^(?P<type_slug>[\w\-]+)/$', 'ad_by_type', name='sponsorship_ad_by_type'),
)