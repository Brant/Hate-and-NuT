"""
Comic models
"""
from datetime import datetime

from django.db import models
from django.utils import timezone

from noodles.models import TitleDateSlug, HalfQuarterAssetsMixin


class Comic(TitleDateSlug, HalfQuarterAssetsMixin):
    """
    Represents a comic
    """
    comic_image = models.ImageField(upload_to="images/comics")
    published = models.BooleanField(default=True)
    chronology = models.IntegerField(blank=True, unique=True)
    preview_image = models.ImageField(upload_to="images/preview", help_text="500x500")
    description = models.TextField(help_text="Will show up in feed, meta description, and OG-driven previews")
    single_row = models.BooleanField(default=False, help_text="Is this a single-row, 'wide' comic?")
    
    def is_available_to_public(self):
        """
        Calculate whether or not the comic is
        publicly available - mostly tied to date
        """
        if not self.published:
            return False
        
        return self.date <= timezone.now()
    
    class Meta:
        """
        Django Metadata
        """
        ordering = ["-chronology", ]
        get_latest_by = "chronology"
        
    @models.permalink
    def get_absolute_url(self):
        return ("comic", [str(self.chronology)])
    
    def save(self, *args, **kwargs):
        """
        custom save to assign chronology
        """
        if not self.chronology:
            latest_chronology = Comic.objects.filter(published=True).aggregate(models.Max("chronology"))["chronology__max"]
            if not latest_chronology:
                latest_chronology = 0
            self.chronology = latest_chronology + 1
        super(Comic, self).save(*args, **kwargs)
        