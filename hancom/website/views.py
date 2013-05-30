"""
Views relating to the website itself
"""
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View

from hancom.comics.models import Comic


def homepage(request):
    """
    Website homepage
    """
    latest_comics = Comic.objects.filter(published=True, date__lte=datetime.now())[:2]
    latest_comic = latest_comics[0]
    
    previous_comic = None
    if len(latest_comics) > 1:
        previous_comic = latest_comics[1]

    response_data = {"latest_comic": latest_comic, "previous_comic": previous_comic}
    return render_to_response("website/home.html", response_data, context_instance=RequestContext(request))