"""
Queries for convinience and consistency
"""
from datetime import datetime
from hancom.comics.models import Comic


def published_comics():
    """
    Return all published comics
    """
    return Comic.objects.filter(published=True, date__lte=datetime.now())