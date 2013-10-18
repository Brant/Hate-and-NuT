"""
FEEDS!
"""
from urllib2 import URLError
from socket import timeout

from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.conf import settings

from noodles.feeds import RSSFeedWithContentEncoded

from hancom.website.queries import published_comics


class SiteFeed(RSSFeedWithContentEncoded):
    """
    """
    title = "Adventures of Hate and NuT"
    link = "/"
    description = "A lighthearted webcomic comedy about the adventures of couple of ruthless killers - Hate and NuT - along with a colorful cast of other characters, set in a dangerous fantasy world."


    author_name = "Brant Steen"
    author_email = "hateandnut@gmail.com"
    author_link = "http://hateandnut.com"

    item_author_name = "Brant Steen"
    item_author_email = "hateandnut@gmail.com"
    item_author_link = "http://hateandnut.com"

    def item_guid_is_permalink(self, obj):
        return True

    def items(self):
        return published_comics()[:30]

    def item_title(self, item):
        if item.story_arc and item.special_story_arc_title:
            return item.special_story_arc_title
        return "Hate and NuT #%s" % item.chronology

    def item_pubdate(self, item):
        return item.date

    def item_content_encoded(self, item):
        """
        Full entry content
        """
        return render_to_string("comics/feed/item_description.html", {"comic": item, "SITE_URL": "http://%s" % Site.objects.get_current().domain})
