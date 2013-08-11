"""
Admin configurations for comics
"""
from django.contrib import admin

from hancom.comics.models import Comic, StoryArc


class ComicAdmin(admin.ModelAdmin):
    """
    Custom comic admin
    """
    list_display = ["chronology", "title", "date", "published", ]
    list_display_links = ["title", ]
    list_filter = ["published", "story_arc", ]
    list_editable = ["published", ]

    fieldsets = (
        (None, {
            'fields': ('title', 'description', ),
        }),
        ('Story Arc', {
            'fields': ('story_arc', 'special_story_arc_title'),
            'classes': ('collapse', )
        }),
        ('Publish Details', {
            'fields': ('date', 'published', 'chronology', ),
        }),
        
        ('Images', {
            'fields': ('comic_image', 'preview_image', 'single_row', ),
        }),
        
    )


admin.site.register(StoryArc)
admin.site.register(Comic, ComicAdmin)
