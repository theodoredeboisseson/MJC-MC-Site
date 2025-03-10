from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from apps.common.mixins import ContentMixin
from apps.common.models import DetailPage, BaseIndexPage


class AssociationIndexPage(BaseIndexPage, ContentMixin):
    content_panels = BaseIndexPage.content_panels + ContentMixin.content_panels

    subpage_types = ['association.AssociationPage']

    class Meta:
        verbose_name = "Grille pages de l'Association"


class AssociationPage(DetailPage):
    DetailPage.image.help_text ="Cette image sera utilisée pour la vignette dans la page d'index",
    show_image_in_page = models.BooleanField(
        default=True,
        verbose_name="Afficher l'image dans la page",
        help_text="Décochez pour afficher l'image uniquement dans la grille de la page parente"
    )

    content_panels = DetailPage.content_panels + [
        FieldPanel('show_image_in_page'),
    ]

    class Meta:
        verbose_name = "Page Association"
