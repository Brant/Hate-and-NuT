"""
Comic views
"""
from datetime import datetime

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from hancom.comics.models import Comic, StoryArc
from hancom.comics.util import get_previous_next_comics


def storyarc_redirect(request, arc_slug):
    """
    Story arcs don't really have their own URL
        They just redirect to the first comic
        in the arc
    """
    try:
        arc = StoryArc.objects.prefetch_related("comic_set").get(slug=arc_slug)
    except ObjectDoesNotExist:
        raise Http404

    comics = arc.comic_set.filter(published=True, date__lte=datetime.now()).reverse()

    return HttpResponseRedirect(comics[0].get_absolute_url())


def archive_index(request):
    """
    History of comic releases
    """
    comics = Comic.objects.filter(published=True, date__lte=datetime.now())
    archives = comics.reverse().dates("date", "month")
    story_arcs = StoryArc.objects.prefetch_related("comic_set").filter(complete=True)
    response_data = {"comics": comics, "archives": archives, "story_arcs": story_arcs}
    return render_to_response("comics/archive_index.html", response_data, context_instance=RequestContext(request))


def comic_page(request, comic_id):
    """
    A publishd comic

    comic_id is actually chronological sequence
    """
    comic_id = int(comic_id)

    try:
        comic = Comic.objects.prefetch_related("story_arc").get(chronology=comic_id, published=True)
    except ObjectDoesNotExist:
        raise Http404

    if not comic.is_available_to_public():
        if not request.user.is_authenticated():
            raise Http404

    previous_comic, next_comic = get_previous_next_comics(comic_id)

    response_data = {"comic": comic, "previous_comic": previous_comic, "next_comic": next_comic}

    return render_to_response("comics/comic_page.html", response_data, context_instance=RequestContext(request))
