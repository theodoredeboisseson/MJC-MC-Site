from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from modelcluster.fields import ParentalKey


class RotatingWord(models.Model):
    page = ParentalKey('home.PageDAcceuil', related_name='rotating_words', on_delete=models.CASCADE)
    word = models.CharField(max_length=255, default="de l'Art")

    panels = [
        FieldPanel('word'),
    ]

    def __str__(self):
        return self.word

class PageDAcceuil(Page):
    intro_title = models.CharField(max_length=255)
    hero_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    def get_latest_events(self):
        from apps.agenda.models import get_events
        from django.utils import timezone
        from django.db.models import Q
        return get_events(date_filter=Q(date__gte=timezone.now()), sort_by='date')[:3]

    content_panels = Page.content_panels + [
        FieldPanel('intro_title'),
        FieldPanel('hero_image'),
        InlinePanel('rotating_words', label="Mot à défiler"),
    ]