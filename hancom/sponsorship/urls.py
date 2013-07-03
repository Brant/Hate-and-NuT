"""
URL configurations for sposorships
"""
from django.conf.urls import patterns, include, url


urlpatterns = patterns('hancom.sponsorship.views',
    url(r'^(?P<type_slug>[\w\-]+)/$', 'ad_by_type', name='sponsorship_ad_by_type'),
    url(r'^form/advertise/$', 'get_advertise_form', name='sponsorship_advertise_form'),
    url(r'^form/sponsor/$', 'get_sponsor_form', name='sponsorship_sponsor_form'),
    url(r'^form/inquiry/submit/$', 'save_inquiry', name='sponsorship_save_inquiry'),
)