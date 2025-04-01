from django.shortcuts import render
from wagtail.models import Page

def sitemap(request):
    pages = Page.objects.live().public().exclude(depth=1).order_by('path')
    for page in pages:
        page.margin_left = 2 * page.depth
    return render(request, 'home/sitemap.html', {'pages': pages})