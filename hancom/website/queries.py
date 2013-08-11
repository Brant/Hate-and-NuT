"""
Queries for convinience and consistency
"""
from datetime import datetime
from hancom.comics.models import Comic


def published_comics():
    """
    Return all published comics
    """
    return Comic.objects.select_related('story_arc').filter(published=True, date__lte=datetime.now())