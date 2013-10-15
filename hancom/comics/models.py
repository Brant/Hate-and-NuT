"""
Comic models
"""
from django.db import models
from django.utils import timezone

from hancom.characters.models import Character

from noodles.models import TitleDateSlug, HalfQuarterAssetsMixin, NameSlug


class StoryArc(NameSlug):
    """
    """
    complete = models.DateTimeField(null=True)

    @models.permalink
    def get_absolute_url(self):
        return ("comic_story_redirect", [str(self.slug)])


class Comic(TitleDateSlug, HalfQuarterAssetsMixin):
    """
    Represents a comic
    """
    description = models.TextField(help_text="Will show up in feed, meta description, and OG-driven previews")

    comic_image = models.ImageField(upload_to="images/comics")
    preview_image = models.ImageField(upload_to="images/preview", help_text="500x500")

    original_comic = models.ImageField(upload_to="images/comics/originals", null=True, blank=True)

    published = models.BooleanField(default=True)
    chronology = models.IntegerField(blank=True, unique=True)

    single_row = models.BooleanField(default=False, help_text="Is this a single-row, 'wide' comic?")

    special_story_arc_title = models.CharField(max_length=300, null=True, blank=True, help_text="Will override 'Hate and NuT #X' if part of a story arc")
    story_arc = models.ForeignKey(StoryArc, null=True, blank=True)

    continuation_of = models.ForeignKey('self', null=True, blank=True)

    characters = models.ManyToManyField(Character, null=True, blank=True, help_text="Characters that appear in this comic")

    def inside_arc(self):
        """
        Is the instance inside a story arc

        Returns True/False
        """
        if not self.story_arc:
            return False

        in_arc = self.story_arc.comic_set.filter(published=True).order_by("chronology")

        return list(in_arc).index(self) > 0

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
    def get_preview_absolute_url(self):
        """
        Permalink to logged-in preview
        """
        return ("comic_preview", [str(self.chronology)])

    @models.permalink
    def get_original_absolute_url(self):
        """
        Permalink to original comic
        """
        return ("comic_original", [str(self.chronology)])

    @models.permalink
    def get_absolute_url(self):
        """
        Permalink, based on chronology
        """
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
