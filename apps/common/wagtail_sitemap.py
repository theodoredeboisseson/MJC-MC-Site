from django.contrib.sitemaps import Sitemap
from wagtail.models import Page

class WagtailPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Page.objects.live().public()

    def location(self, item):
        return item.url