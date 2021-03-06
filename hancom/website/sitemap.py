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
            Page("Archive", reverse("archive_index"), published_comics()[0].date, ".7", "daily"),
            # Page("Donate", reverse("donate"), date(2013, 7, 1), ".5", "monthly"),
            Page("Characters", reverse("characters_index"), date(2013, 7, 5), ".5", "monthly"),
            # Page("Advertise", reverse("become_an_advertiser"), date(2013, 7, 1), ".5", "monthly"),
            Page("Sponsor", reverse("become_a_sponsor"), date(2013, 7, 1), ".5", "monthly"),
            Page("Contact", reverse("contact_me"), date(2013, 8, 1), ".5", "monthly"),
        ]

    def location(self, item):
        return item.location

    def lastmod(self, item):
        return item.lastmod

    def priority(self, item):
        return item.priority

    def changefreq(self, item):
        return item.changefreq
