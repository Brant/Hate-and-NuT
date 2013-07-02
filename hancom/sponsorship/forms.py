"""
Sponsorship Forms
"""
from django import forms

from hancom.sponsorship.models import SponsorshipInquiry


class AdInquiryForm(forms.ModelForm):
    
    class Meta:
        """
        Django Metadata
        """
        model = SponsorshipInquiry