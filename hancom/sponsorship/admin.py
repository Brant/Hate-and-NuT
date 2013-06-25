"""
Admin configurations
"""
from django.contrib import admin

from hancom.sponsorship.models import Campaign, Ad, AdType


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


admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Ad)
admin.site.register(AdType)
