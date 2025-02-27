from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class DetailPage(Page):
    subtitle = models.CharField(max_length=250, blank=True, verbose_name="Sous-titre")
    content = RichTextField(
        verbose_name="Contenu",
        blank=True,
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Image"
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('content'),
        FieldPanel('image'),
    ]

    class Meta:
        abstract = True