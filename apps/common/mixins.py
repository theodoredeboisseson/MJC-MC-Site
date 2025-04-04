from django.db import models
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class SEOMixin(models.Model):
    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="Mots-clés spécifiques à cette page séparés par des virgules"
    )

    seo_panels = [
        MultiFieldPanel([
            FieldPanel('seo_keywords'),
        ], heading="Mot clés pour les recherches"),
    ]

    class Meta:
        abstract = True

class ContentMixin(models.Model):
    content = RichTextField(
        verbose_name="Contenu",
        blank=True,
    )

    content_panels = [
        FieldPanel('content'),
    ]

    class Meta:
        abstract = True
           
class VilleMixin(models.Model):
    MAUGUIO = 'Mauguio'
    CARNON = 'Carnon'
    BOTH = 'Mauguio et Carnon'
    VILLE_CHOICES = [
        (MAUGUIO, 'Mauguio'),
        (CARNON, 'Carnon'),
        (BOTH, 'Mauguio et Carnon'),
    ]
    ville = models.CharField(
        max_length=17,
        choices=VILLE_CHOICES,
        default=MAUGUIO,
        blank=True
    )
    
    content_panels = [
        FieldPanel('ville'),
    ]
    
    class Meta:
        abstract = True