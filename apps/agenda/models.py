from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import FieldPanel
from django.core.paginator import Paginator

from apps.common.models import DetailPage


class AgendaIndexPage(Page):
    intro = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    def get_events(self):
        # Get list of events ordered by date
        return EventPage.objects.live().order_by('date')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Get all events
        all_events = self.get_events()

        # Paginate events list
        paginator = Paginator(all_events, 9)  # Show 9 events per page
        page = request.GET.get('page')
        events = paginator.get_page(page)

        context['events'] = events
        return context

    class Meta:
        verbose_name = "Page Agenda"

class EventPage(DetailPage):
    date = models.DateTimeField("Date de l'événement")

    content_panels = DetailPage.content_panels + [
        FieldPanel('date'),
    ]

    class Meta:
        verbose_name = "Événement"