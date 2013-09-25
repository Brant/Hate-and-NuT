"""
Custom tags and filters for sponsorship
"""
from datetime import datetime

from django import template


from hancom.comics.models import Comic
from hancom.comics.util import get_random_comic

register = template.Library()


@register.filter
def get_random_comic_link(current_comic):
    comic = get_random_comic(current_comic)
    return comic.get_absolute_url()


@register.inclusion_tag("comics/render/comic_footer.html", takes_context=True)
def render_comic_footer(context, comic, next_comic=None, prev_comic=None):
    return {"comic": comic, "SITE_URL": context["SITE_URL"], "request": context["request"], "next_comic": next_comic, "previous_comic": prev_comic}
