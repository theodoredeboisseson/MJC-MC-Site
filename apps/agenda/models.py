from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import FieldPanel
from django.core.paginator import Paginator
from datetime import datetime

from apps.common.models import DetailPage


class AgendaIndexPage(Page):
    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel('intro')]

    def get_upcoming_events(self, sort_by='date'):
        return EventPage.objects.live().filter(date__gte=datetime.now()).order_by(sort_by, 'title')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        sort_by = request.GET.get('sort_by', 'date')
        paginator = Paginator(self.get_upcoming_events(sort_by), 9)
        context['upcoming_events'] = paginator.get_page(request.GET.get('page'))
        context['past_events_page'] = self.get_children().type(PastEventsPage).live().first()
        context['sort_by'] = sort_by
        return context

    class Meta:
        verbose_name = "Page Agenda"


class PastEventsPage(Page):
    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel('intro')]

    def get_past_events(self, sort_by='-date'):
        return EventPage.objects.live().filter(date__lt=datetime.now()).order_by(sort_by, 'title')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        sort_by = request.GET.get('sort_by', '-date')
        paginator = Paginator(self.get_past_events(sort_by), 9)
        context['past_events'] = paginator.get_page(request.GET.get('page'))
        context['sort_by'] = sort_by
        return context

    class Meta:
        verbose_name = "Événements passés"


class EventPage(DetailPage):
    date = models.DateTimeField("Date de l'événement")

    content_panels = DetailPage.content_panels + [FieldPanel('date')]

    class Meta:
        verbose_name = "Événement"
