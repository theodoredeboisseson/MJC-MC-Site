from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from modelcluster.fields import ParentalKey

from apps.agenda.models import EventPage, get_future_events
from apps.common.models import BasePage


class RotatingWord(models.Model):
    page = ParentalKey('home.PageAcceuil', related_name='rotating_words', on_delete=models.CASCADE)
    word = models.CharField(max_length=255, default="de l'Art")

    panels = [
        FieldPanel('word'),
    ]

    def __str__(self):
        return self.word

class PageAcceuil(BasePage):
    intro_title = models.CharField(max_length=255, verbose_name="Titre d'introduction", default="Bienvenue à la MJC")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image de fond'
    )
    video_url = models.URLField(
        verbose_name="URL de la vidéo YouTube",
        help_text="Collez l'URL de la vidéo YouTube (format embed)",
        blank=True,
        null=True
    )
    extra_content = RichTextField(
        blank=True,
        null=True,
        verbose_name="Contenu optionnel",
        help_text="Message spécial à en dessous de la section d'introduction"
    )

    def get_future_events(self):
        return get_future_events(3)

    content_panels = Page.content_panels + [
        FieldPanel('intro_title'),
        FieldPanel('hero_image'),
        FieldPanel('video_url'),
        FieldPanel('extra_content'),
        InlinePanel('rotating_words', label="Mot à défiler"),
    ]

    class Meta:
        verbose_name = "Page d'Accueil"