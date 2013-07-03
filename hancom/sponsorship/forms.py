"""
Sponsorship Forms
"""
from django import forms

from hancom.sponsorship.models import SponsorshipInquiry

from noodles.forms import EmailInput




class InquiryForm(forms.ModelForm):
    name = forms.CharField(label="Your name", help_text="So I know what to call you")
    email = forms.CharField(label="Your email", help_text="So I can contact you", widget=EmailInput())
    description = forms.CharField(label="Some information", help_text="Tell me a little bit about you'd like to promote", widget=forms.Textarea())
    type = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        """
        Django Metadata
        """
        model = SponsorshipInquiry
