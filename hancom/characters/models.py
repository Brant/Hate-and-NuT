"""
Character Models
"""
from django.db import models

from noodles.models import NameSlugActive, HalfQuarterAssetsMixin


class Character(NameSlugActive, HalfQuarterAssetsMixin):
    """
    Represents a character in the comic

    Active = True -> display
    Active = False -> "Hide"
    """
    description = models.TextField()
    index = models.IntegerField(default=0, help_text="Order to be displayed")
    image = models.ImageField(upload_to="characters/images")
    show_first_date = models.DateTimeField(null=True, blank=True, help_text="When to 'release' this chararcter")

    class Meta:
        """
        Django Metadata
        """
        ordering = ["-show_first_date", "index", "name"]
