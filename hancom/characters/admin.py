from django.contrib import admin

from hancom.characters.models import Character


class CharacterAdmin(admin.ModelAdmin):
    """
    Admin config for administiring character listings
    """
    list_display = ["name", "show_first_date", "index", "active", ]
    list_filter = ["active", ]
    list_editable = ["active", ]
    

admin.site.register(Character, CharacterAdmin)