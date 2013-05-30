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


def comic_page(request, comic_id):
    """
    A publishd comic
    """
    comic_id = int(comic_id)
    
    try:
        comic = Comic.objects.get(chronology=comic_id, published=True, date__lte=datetime.now())
    except ObjectDoesNotExist:
        raise Http404
    
    try:
        previous_comic = Comic.objects.filter(chronology__lt=comic_id, published=True, date__lte=datetime.now())[:1][0]
    except IndexError:
        previous_comic = None
    
    try:
        next_comic = Comic.objects.filter(chronology__gt=comic_id, published=True, date__lte=datetime.now()).order_by("chronology")[:1][0]
    except IndexError:
        next_comic = None
        
    response_data = {"comic": comic, "previous_comic": previous_comic, "next_comic": next_comic}
    
    return render_to_response("comics/comic_page.html", response_data, context_instance=RequestContext(request))