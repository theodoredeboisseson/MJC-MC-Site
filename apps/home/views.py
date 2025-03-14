from django.shortcuts import render
from wagtail.models import Page

def sitemap(request):
    pages = Page.objects.live().public().exclude(depth=1).order_by('path')
    for page in pages:
        page.font_size = 5 / page.depth if page.depth != 0 else 1.2
        page.margin_left = 2 * page.depth
    return render(request, 'home/sitemap.html', {'pages': pages})