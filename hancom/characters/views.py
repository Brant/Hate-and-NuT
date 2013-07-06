from datetime import datetime
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

from hancom.characters.models import Character

def character_index(request):
    """
    List of characters
    """
    print "############### HI"
    characters = Character.objects.filter(Q(show_first_date__lte=datetime.now()) | Q(show_first_date__isnull=True), active=True)
    print characters
    response_data = {"characters": characters}
    return render_to_response("characters/index.html", response_data, context_instance=RequestContext(request))