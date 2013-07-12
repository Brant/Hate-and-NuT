"""
Comic views
"""
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View
from django.core.exceptions import ObjectDoesNotExist

from hancom.comics.models import Comic
from hancom.comics.util import get_previous_next_comics


def archive_index(request):
    """
    """
    comics = Comic.objects.filter(published=True, date__lte=datetime.now())
    archives = comics.dates("date", "month").reverse()
    response_data = {"comics": comics, "archives": archives}
    return render_to_response("comics/archive_index.html", response_data, context_instance=RequestContext(request))


def comic_page(request, comic_id):
    """
    A publishd comic
    
    comic_id is actually chronological sequence
    """
    comic_id = int(comic_id)
    
    try:
        comic = Comic.objects.get(chronology=comic_id, published=True)
    except ObjectDoesNotExist:
        raise Http404
    
    if not comic.is_available_to_public():
        if not request.user.is_authenticated():
            raise Http404
    
    previous_comic, next_comic = get_previous_next_comics(comic_id)
        
    response_data = {"comic": comic, "previous_comic": previous_comic, "next_comic": next_comic}
    
    return render_to_response("comics/comic_page.html", response_data, context_instance=RequestContext(request))