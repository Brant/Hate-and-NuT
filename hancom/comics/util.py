"""
Utility functions for comics
"""
from datetime import datetime

from django.db.models import Q

from hancom.comics.models import Comic



def get_previous_next_comics(chronology):
    """
    Based on a comic ID, return
    the (previous, next) comics that are available
    """
    try:
        previous_comic = Comic.objects.filter(chronology__lt=chronology, published=True, date__lte=datetime.now())[:1][0]
    except IndexError:
        previous_comic = None

    try:
        next_comic = Comic.objects.filter(chronology__gt=chronology, published=True, date__lte=datetime.now()).order_by("chronology")[:1][0]
    except IndexError:
        next_comic = None

    return (previous_comic, next_comic)


def get_random_comic(comic=None):
    """
    return a random comic that is not 'comic'
    """
    if comic:
        return Comic.objects.filter(~Q(id=comic.id), published=True, date__lte=datetime.now()).order_by("?")[0]

    return Comic.objects.filter(published=True, date__lte=datetime.now()).order_by("?")[0]
