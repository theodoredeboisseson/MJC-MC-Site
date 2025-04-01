from django.core.exceptions import ValidationError
from wagtail.models import Page
from django.db import models
from wagtail.admin.panels import FieldPanel
from django.core.paginator import Paginator
from django.utils import timezone

from apps.common.mixins import VilleMixin
from apps.common.models import DetailPage, BasePage


def get_events(date_filter, sort_by, villes=None):
    events = EventPage.objects.live().filter(date_filter)
    if villes:
        ville_list = villes.split(',')
        if len(ville_list) == 2:  # Si les deux villes sont sélectionnées
            events = events.filter(models.Q(ville__in=ville_list) | models.Q(ville=EventPage.BOTH))
        else:
            events = events.filter(models.Q(ville=ville_list[0]) | models.Q(ville=EventPage.BOTH))
    return events.order_by(sort_by, 'title')

def get_future_events(limit=5):
    return EventPage.objects.live().filter(start_date__gte=timezone.now()).order_by('start_date')[:limit]


class EventListPage(BasePage):
    intro = models.TextField(blank=True)
    content_panels = BasePage.content_panels + [FieldPanel('intro')]

    def get_events_context(self, request, date_filter, default_sort):
        context = {}
        sort_by = request.GET.get('sort_by', default_sort)
        villes = request.GET.get('ville', '')
        search_query = request.GET.get('search', '')
    
        # Validate sort_by
        if sort_by not in ['start_date', 'title', 'end_date']:
            sort_by = default_sort
    
        # Validate villes
        if villes:
            ville_list = villes.split(',')
            for ville in ville_list:
                if ville not in [EventPage.MAUGUIO, EventPage.CARNON, EventPage.BOTH]:
                    villes = ''
                    break
    
        events = get_events(date_filter, sort_by, villes)
    
        if search_query:
            events = events.filter(title__icontains=search_query)
    
        paginator = Paginator(events, 9)
        context['sort_by'] = sort_by
        context['villes'] = villes.split(',') if villes else []
        context['search_query'] = search_query
        return context, paginator

    class Meta:
        abstract = True

class AgendaIndexPage(EventListPage):
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        filter_type = request.GET.get('filter')

        # Filtrage des événements en fonction de la date
        if filter_type == 'past':
            events = EventPage.objects.live().filter(start_date__lt=timezone.now()).order_by('-start_date')
            context['showing_past'] = True
        else:
            events = EventPage.objects.live().filter(start_date__gte=timezone.now()).order_by('start_date')
            context['showing_past'] = False

        # Pagination (10 événements par page)
        paginator = Paginator(events, 10)
        context['event_list'] = paginator.get_page(request.GET.get('page'))

        # Générer l'URL du bouton toggle
        context['toggle_url'] = f"{self.url}?filter={'upcoming' if context['showing_past'] else 'past'}"

        return context

    class Meta:
        verbose_name = "Page Agenda"


class EventPage(DetailPage, VilleMixin):
    start_date = models.DateField(
        "Date de début",
        help_text="Date de début de l'événement",
        default=timezone.now
    )
    end_date = models.DateField(
        "Date de fin",
        blank=True,
        null=True,
        help_text="Date de fin de l'événement (laisser vide si l'événement dure un seul jour)"
    )

    content_panels = DetailPage.content_panels + VilleMixin.content_panels + [
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('ville'),
    ]

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("La date de fin ne peut pas être antérieure à la date de début.")

    class Meta:
        verbose_name = "Événement"
