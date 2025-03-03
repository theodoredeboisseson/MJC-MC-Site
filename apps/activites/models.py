from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet

from apps.common.models import DetailPage

@register_snippet
class Animateur(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class SubActivity(Orderable):
    page = ParentalKey('activites.ActivityPage', related_name='sub_activities', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.title

class ActivityPage(DetailPage):
    DetailPage.content.verbose_name = "Description"
    animateurs = ParentalManyToManyField('activites.Animateur', blank=True)
    link = models.URLField(
        max_length=200,
        help_text="Lien de redirection pour le bouton",
        blank=True,
    )

    content_panels = DetailPage.content_panels + [
        FieldPanel('animateurs', widget=CheckboxSelectMultiple),
        InlinePanel('sub_activities', label="Sous Activités"),
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