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


class OriginalComicsSitemap(ComicsSitemap):
    """
    Sitemap for Original comics
    """
    priority = "0.5"

    def items(self):
        return super(OriginalComicsSitemap, self).items().filter(original_comic__isnull=False)

    def location(self, obj):
        return obj.get_original_absolute_url()
