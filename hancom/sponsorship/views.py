"""
Sponsorship Views
"""
from random import choice
from datetime import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import mail_admins
from django.views.decorators.cache import never_cache

from hancom.sponsorship.models import Ad
from hancom.sponsorship.forms import InquiryForm


def save_inquiry(request):
    """
    Handle POST data (via ajax) for SponsorshipInquiry forms
    """
    if not request.is_ajax():
        raise Http404
    
    if not request.method == "POST":
        raise Http404
    
    form = InquiryForm(request.POST)
    
    if form.is_valid():
        inquiry = form.save()
        mail_admins(subject="%s Inquiry" % inquiry.get_type_display(), message=render_to_string("sponsorship/email/sponsorship_inquiry_notification.txt", {"inquiry": inquiry}))
        return render_to_response("sponsorship/forms/inquiry_thanks.html", {}, context_instance=RequestContext(request))
    
    return render_to_response("sponsorship/forms/inquiry.html", {"form": form}, context_instance=RequestContext(request))


def get_advertise_form(request):
    """
    Get the form for inquiring about advertising
    """
    if not request.is_ajax():
        raise Http404
    
    form = InquiryForm(initial={"type": "A"})
    return render_to_response("sponsorship/forms/inquiry.html", {"form": form}, context_instance=RequestContext(request))


def get_sponsor_form(request):
    """
    Get the form for inquiring about becoming a sponsor
    """
    if not request.is_ajax():
        raise Http404
    
    form = InquiryForm(initial={"type": "S"})
    return render_to_response("sponsorship/forms/inquiry.html", {"form": form}, context_instance=RequestContext(request))


@never_cache
def ad_by_type(request, type_slug):
    """
    
    """
#     if not request.is_ajax():
#         raise Http404
    
    possible_ads = Ad.objects.prefetch_related("type", "campaign").filter(
        Q(campaign__start_date__gte=datetime.now()) | Q(campaign__start_date__isnull=True), 
        Q(campaign__end_date__lte=datetime.now()) | Q(campaign__end_date__isnull=True),
        Q(start_date__gte=datetime.now()) | Q(start_date__isnull=True),
        Q(end_date__lte=datetime.now()) | Q(end_date__isnull=True),
        campaign__active=True, active=True,
        type__slug=type_slug
    )
    
    if not possible_ads:
        return HttpResponse("")
    
    response_data = {"ad": choice(possible_ads)}
    return render_to_response("sponsorship/ad.html", response_data, context_instance=RequestContext(request))
