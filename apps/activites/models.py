from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from apps.common.models import DetailPage


class TimeSlot(models.Model):
    label = models.CharField(max_length=100, help_text="Ex: Niveau Débutant")
    start_time = models.TimeField()
    end_time = models.TimeField()

    panels = [
        FieldPanel('label'),
        FieldPanel('start_time'),
        FieldPanel('end_time'),
    ]

    def __str__(self):
        return f"{self.label}: {self.start_time.strftime('%H:%M')}-{self.end_time.strftime('%H:%M')}"

    class Meta:
        abstract = True

class ActivityTimeSlot(TimeSlot):
    activity = ParentalKey(
        'ActivityPage',
        on_delete=models.CASCADE,
        related_name='time_slots'
    )
    days = models.CharField(
        max_length=255,
        help_text="Ex: Lundi au Vendredi, ou Mardi/Jeudi"
    )

    panels = TimeSlot.panels + [
        FieldPanel('days'),
    ]

class ActivityPage(DetailPage):
    DetailPage.content.verbose_name = "Description"
    instructors = models.CharField(
        max_length=255,
        help_text="Nom du/des animateur(s)",
        blank=True,
    )
    price_resident = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Prix pour les résidents Mauguio/Carnon",
        null=True,
    )
    price_non_resident = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Prix pour les non-résidents",
        null=True,
    )

    content_panels = DetailPage.content_panels + [
        FieldPanel('instructors'),
        MultiFieldPanel([
            FieldPanel('price_resident'),
            FieldPanel('price_non_resident'),
        ], heading="Tarifs"),
        InlinePanel('time_slots', label="Horaires"),
    ]

    class Meta:
        verbose_name = "Activité"


class ActivityList(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['activities'] = ActivityPage.objects.live().order_by('title')
        return context

    class Meta:
        verbose_name = "Liste des Activités"


# class ActivityPage(Page):
#     description = models.TextField()
#     price_resident = models.DecimalField(max_digits=6, decimal_places=2)
#     price_non_resident = models.DecimalField(max_digits=6, decimal_places=2)
#     instructors = models.CharField(max_length=255)
# 
#     content_panels = Page.content_panels + [
#         FieldPanel('description'),
#         MultiFieldPanel([
#             InlinePanel('time_slots', label="Time Slots"),
#         ], heading="Time Slots"),
#         MultiFieldPanel([
#             FieldPanel('price_resident'),
#             FieldPanel('price_non_resident'),
#         ], heading="Prices"),
#         FieldPanel('instructors'),
#     ]