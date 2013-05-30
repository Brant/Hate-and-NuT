"""
Comic models
"""
from django.db import models

from noodles.models import TitleDateSlug, HalfQuarterAssetsMixin


class Comic(TitleDateSlug, HalfQuarterAssetsMixin):
    """
    Represents a comic
    """
    comic_image = models.ImageField(upload_to="images/comics")
    published = models.BooleanField(default=True)
    chronology = models.IntegerField(blank=True, unique=True)
    
    class Meta:
        """
        Django Metadata
        """
        ordering = ["-chronology", ]
        get_latest_by = "chronology"
        
    @models.permalink
    def get_absolute_url(self):
        return ("comic", str(self.pk))
    
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
        