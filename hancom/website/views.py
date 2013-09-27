"""
Views relating to the website itself
"""
from datetime import datetime

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.base import View

from hancom.comics.models import Comic
from hancom.website.queries import published_comics
from hancom.website.forms import HancomContactForm


def get_contact_form(request):
    """
    Get the form for inquiring about advertising
    """
    if not request.is_ajax():
        raise Http404

    form = HancomContactForm()
    return render_to_response("website/forms/contact.html", {"form": form}, context_instance=RequestContext(request))


def contact_submit(request):
    """
    Handle contact submission
    """
    if not request.is_ajax():
        raise Http404

    form = HancomContactForm(request.POST)

    if not form.is_valid():
        return render_to_response("website/forms/contact.html", {"form": form}, context_instance=RequestContext(request))

    form.save()
    return render_to_response("website/forms/contact_thanks.html", {}, context_instance=RequestContext(request))



def donate(request):
    """
    Displays donation form
    """
    response_data = {}
    return render_to_response("website/donate.html", response_data, context_instance=RequestContext(request))


def homepage(request):
    """
    Website homepage
    """
    latest_comics = published_comics()[:2]
    latest_comic = latest_comics[0]

    previous_comic = None
    if len(latest_comics) > 1:
        previous_comic = latest_comics[1]

    response_data = {"latest_comic": latest_comic, "previous_comic": previous_comic}
    return render_to_response("website/home.html", response_data, context_instance=RequestContext(request))
