from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from apps.common.models import DetailPage


class ActivityPage(DetailPage):
    DetailPage.content.verbose_name = "Description"
    instructors = models.CharField(
        max_length=255,
        help_text="Nom du/des animateur(s)",
        blank=True,
    )
    price_resident = models.CharField(
        max_length=50,
        help_text="Prix pour les résidents Mauguio/Carnon",
        null=True,
    )
    price_non_resident = models.CharField(
        max_length=50,
        help_text="Prix pour les non-résidents",
        null=True,
    )
    link = models.URLField(
        max_length=200,
        help_text="Lien de redirection pour le bouton",
        blank=True,
    )

    content_panels = DetailPage.content_panels + [
        FieldPanel('instructors'),
        MultiFieldPanel([
            FieldPanel('price_resident'),
            FieldPanel('price_non_resident'),
        ], heading="Tarifs"),
        FieldPanel('link'),
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