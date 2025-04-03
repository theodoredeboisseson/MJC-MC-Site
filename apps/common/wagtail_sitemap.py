from django.contrib.sitemaps import Sitemap
from wagtail.models import Page

class WagtailPageSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return Page.objects.live().public().filter(depth__gt=1)

    def location(self, item):
        return item.url if item.url else ''

    def priority(self, item):
        # Calcul de la profondeur de la page
        depth = item.depth

        # Attribution de la priorité en fonction de la profondeur
        if depth <= 2:  # Page d'accueil
            return 1.0
        elif depth == 3:  # Pages de niveau supérieur
            return 0.8
        elif depth == 4:  # Pages de niveau intermédiaire
            return 0.6
        else:  # Pages de niveau inférieur
            return 0.4