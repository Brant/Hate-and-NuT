"""
Sitemap for comics
"""
from django.contrib.sitemaps import Sitemap

from hancom.website.queries import published_comics


class ComicsSitemap(Sitemap):
    """
    Sitemap for comic entries
    """
    changefreq = "monthly"
    priority = "0.8"

    def items(self):
        return published_comics()

    def lastmod(self, obj):
        return obj.date
