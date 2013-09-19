"""
Admin configurations for comics
"""
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

from hancom.comics.models import Comic, StoryArc


class ComicInlineAdmin(admin.TabularInline):
    """
    Show a streamlined admin for comics in story arcs
    """
    model = Comic
    fields = ('title', 'date', 'special_story_arc_title', 'edit_document')
    readonly_fields = ('edit_document', )
    extra = 0
    can_delete = False


    def edit_document(self, instance):
        """
        Convinience link to the admin editor for an FUTP document
            linked to from another FUTP document
        """
        url = "N/A"
        if instance:
            url = reverse("admin:comics_comic_change", args=[instance.pk])
            url = "<a href='%s'>Edit '%s'</a>" % (url, instance.title)
            url = mark_safe(url)
        return url


class StoryArcAdmin(admin.ModelAdmin):
    """
    Custom admin for story arcs
    """
    list_display = ["name", "complete", ]
    list_editable = ["complete", ]
    inlines = [ComicInlineAdmin, ]


class ComicAdmin(admin.ModelAdmin):
    """
    Custom comic admin
    """
    list_display = ["chronology", "title", "date", "published", ]
    list_display_links = ["title", ]
    list_filter = ["published", "story_arc", ]
    list_editable = ["published", ]
    filter_horizontal = ["characters", ]
    fieldsets = (
        (None, {
            'fields': ('title', 'description', ),
        }),
        ('Story Arc', {
            'fields': ('story_arc', 'special_story_arc_title'),
            'classes': ('collapse', )
        }),
        ('Publish Details', {
            'fields': ('date', 'published', 'chronology', 'continuation_of'),
        }),

        ('Images', {
            'fields': ('comic_image', 'preview_image', 'single_row', ),
        }),

        ('Metadata', {
            'fields': ('characters', ),
        }),

    )


admin.site.register(StoryArc, StoryArcAdmin)
admin.site.register(Comic, ComicAdmin)
