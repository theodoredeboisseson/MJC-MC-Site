from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import FieldPanel
from django.core.paginator import Paginator
from datetime import datetime

from apps.common.models import DetailPage


def get_filtered_events(date_filter, sort_by, villes=None):
    events = EventPage.objects.live().filter(date_filter)
    if villes:
        ville_list = villes.split(',')
        events = events.filter(
            models.Q(ville__in=ville_list) | models.Q(ville=EventPage.BOTH)
            if len(ville_list) == 2
            else models.Q(ville=ville_list[0]) | models.Q(ville=EventPage.BOTH)
        )
    return events.order_by(sort_by, 'title')


class EventListPage(Page):
    intro = models.TextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel('intro')]

    def get_events_context(self, request, date_filter, default_sort):
        sort_by = request.GET.get('sort_by', default_sort)
        villes = request.GET.get('ville', '')
        events = get_filtered_events(date_filter, sort_by, villes)
        return {
            'sort_by': sort_by,
            'villes': villes.split(',') if villes else []
        }, Paginator(events, 9)

    class Meta:
        abstract = True


class AgendaIndexPage(EventListPage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        events_context, paginator = self.get_events_context(
            request, models.Q(date__gte=datetime.now()), 'date'
        )
        context.update(events_context)
        context['upcoming_events'] = paginator.get_page(request.GET.get('page'))
        context['past_events_page'] = self.get_children().type(PastEventsPage).live().first()
        return context

    class Meta:
        verbose_name = "Page Agenda"


class PastEventsPage(EventListPage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        events_context, paginator = self.get_events_context(
            request, models.Q(date__lt=datetime.now()), '-date'
        )
        context.update(events_context)
        context['past_events'] = paginator.get_page(request.GET.get('page'))
        return context

    class Meta:
        verbose_name = "Événements passés"


class EventPage(DetailPage):
    VILLE_CHOICES = [
        ('Mauguio', 'Mauguio'),
        ('Carnon', 'Carnon'),
        ('Mauguio et Carnon', 'Mauguio et Carnon'),
    ]

    date = models.DateTimeField("Date de l'événement")
    ville = models.CharField(max_length=10, choices=VILLE_CHOICES, default='Mauguio')
    content_panels = DetailPage.content_panels + [FieldPanel('date'), FieldPanel('ville')]

    class Meta:
        verbose_name = "Événement"
