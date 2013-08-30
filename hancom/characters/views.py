"""
Character Views
"""
from datetime import datetime
from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

from hancom.characters.models import Character


def character_index(request):
    """
    List of characters
    """
    characters = Character.objects.filter(Q(show_first_date__lte=datetime.now()) | Q(show_first_date__isnull=True), active=True)

    if request.GET.get("showall", None):
        if request.user.is_authenticated():
            characters = Character.objects.filter(active=True)

    response_data = {"characters": characters}
    return render_to_response("characters/index.html", response_data, context_instance=RequestContext(request))
