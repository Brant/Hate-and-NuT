"""
Website sitemap
"""
from datetime import date
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from hancom.website.queries import published_comics


class Page(object):
    """
    Simple object to hold attributes for 
        webpage sitemap entries
    """
    def __init__(self, name, location, lastmod, priority, changefreq):
        self.name = name
        self.location = location
        self.lastmod = lastmod
        self.priority = priority
        self.changefreq = changefreq


class WebsiteSitemap(Sitemap):
    """
    Sitemap for non-dynamic, website pages
    """
    def items(self):
        return [
            Page("Homepage", reverse("home"), published_comics()[0].date, "1.0", "daily"),
#             Page("About Hate and NuT", reverse("about"), date(2013, 6, 1), ".4", "never"),
        ]
    
    def location(self, item):
        return item.location
    
    def lastmod(self, item):
        return item.lastmod
    
    def priority(self, item):
        return item.priority
    
    def changefreq(self, item):
        return item.changefreq
        