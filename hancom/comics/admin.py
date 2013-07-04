"""
Admin configurations for comics
"""
from django.contrib import admin

from hancom.comics.models import Comic


class ComicAdmin(admin.ModelAdmin):
    """
    Custom comic admin
    """
    list_display = ["chronology", "title", "date", "published", ]
    list_display_links = ["title", ]
    list_filter = ["published", ]
    list_editable = ["published", ]


admin.site.register(Comic, ComicAdmin)
