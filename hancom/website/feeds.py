"""
FEEDS!
"""
from datetime import datetime 

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.contrib.markup.templatetags.markup import markdown
from django.template.loader import render_to_string
from django.contrib.sites.models import Site

from noodles.feeds import RSSFeedWithContentEncoded

from hancom.comics.models import Comic
from hancom.website.queries import published_comics

class SiteFeed(RSSFeedWithContentEncoded):
    """
    """
    title = "The Adventures of Hate and NuT"
    link = "/"
    description = "A webcomic set in the world of Ultima Online"
    
    
    def items(self):
        return published_comics()[:30]
    
    def item_title(self, item):
        return "Hate and NuT #%s" % item.chronology
    
    def item_pubdate(self, item):
        return item.date
    
    def item_content_encoded(self, item):
        """
        Full entry content
        """
        return render_to_string("comics/feed/item_description.html", {"comic": item, "SITE_URL": "http://%s" % Site.objects.get_current().domain})
    
