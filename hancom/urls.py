"""
Main URL configuraitons for hancom
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from hancom.comics.sitemap import ComicsSitemap
from noodles.urls import favicon_patterns

from hancom.website.feeds import SiteFeed
from hancom.website.sitemap import WebsiteSitemap


admin.autodiscover()


sitemaps = {"website": WebsiteSitemap, "comics": ComicsSitemap, }


urlpatterns = patterns('',
    url(r'^$', 'hancom.website.views.homepage', name='home'),
    url(r'^donate/$', 'hancom.website.views.donate', name='donate'),
    url(r'^advertise/$', TemplateView.as_view(template_name="website/advertise.html"), name='become_an_advertiser'),
    url(r'^sponsor/$', TemplateView.as_view(template_name="website/sponsor.html"), name='become_a_sponsor'),
    (r'^comic/', include("hancom.comics.urls")),
    (r'^sponsorship/', include("hancom.sponsorship.urls")),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url (r'^feed/$', SiteFeed()),
)

if settings.DEBUG:
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += favicon_patterns
    urlpatterns += patterns('',
        url(r'404\.html$', TemplateView.as_view(template_name="404.html"), name="404"),
    )