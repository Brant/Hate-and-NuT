"""
Sponsorship Models
"""
from django.db import models
from noodles.models import TitleDateSlug, NameSlugActive, LittleSlugger, NameSlug


class SponsorshipInquiry(models.Model):
    """
    
    """
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    type = models.CharField(max_length=1, choices=(("A", "Advertising"), ("S", "Sponsorship")))
    description = models.TextField()
    
    

class AdType(NameSlug):
    """
    Represents an ad type
        e.g. 'header banner' or 'large square'
    """
    width = models.IntegerField()
    height = models.IntegerField()


class Campaign(LittleSlugger):
    """
    Represents a sponsorship campaign
        for one patron
    """
    title = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def get_slug_target(self):
        """
        Implementing required method
        """
        return 'title'


class Ad(NameSlugActive):
    """
    Ads have an optional start/end date.
        It's the date range that the ad will show during its campaign.
        These dates should be inside the date range of their campaign.
    """
    type = models.ForeignKey(AdType)
    campaign = models.ForeignKey(Campaign)
    image = models.ImageField(upload_to="sponsorship/ads/images")
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    link = models.CharField(max_length=1000)
