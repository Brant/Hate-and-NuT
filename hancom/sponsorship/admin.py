"""
Admin configurations
"""
from django.contrib import admin

from hancom.sponsorship.models import Campaign, Ad, AdType, SponsorshipInquiry


class AdAdmin(admin.ModelAdmin):
    """
    Configure individual ads
    """
    list_filter = ['type', ]


class AdInlineAdmin(admin.TabularInline):
    """
    Inline ad configration for campaigns
    """
    model = Ad


class CampaignAdmin(admin.ModelAdmin):
    """
    Configure campaign
    """
    inlines = [AdInlineAdmin, ]
    list_display = ["title", "active", "start_date", "end_date", ]
    list_editable = ["active", ] 


class InquiryAdmin(admin.ModelAdmin):
    """
    Sponsorship Inquiries
    """
    list_display = ["name", "date", "email", "type"]
    list_filter = ["type", ]
    readonly_fields = ["date", ]


admin.site.register(SponsorshipInquiry, InquiryAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Ad)
admin.site.register(AdType)
