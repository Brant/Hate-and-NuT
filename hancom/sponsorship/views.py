from random import choice
from datetime import datetime

from django.db.models import Q

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

from hancom.sponsorship.models import Ad


def ad_by_type(request, type_slug):
    """
    
    """
    if not request.is_ajax():
        raise Http404
    
    possible_ads = Ad.objects.prefetch_related("type", "campaign").filter(
        Q(campaign__start_date__gte=datetime.now()) | Q(campaign__start_date__isnull=True), 
        Q(campaign__end_date__lte=datetime.now()) | Q(campaign__end_date__isnull=True),
        Q(start_date__gte=datetime.now()) | Q(start_date__isnull=True),
        Q(end_date__lte=datetime.now()) | Q(end_date__isnull=True), 
        type__slug=type_slug
    )
    
    if not possible_ads:
        return HttpResponse("")
    
    response_data = {"ad": choice(possible_ads)}
    return render_to_response("sponsorship/ad.html", response_data, context_instance=RequestContext(request))
