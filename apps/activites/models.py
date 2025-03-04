from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet

from apps.common.models import DetailPage, SEOMixin, BasePage


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


class ActivityList(BasePage):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]
    promote_panels = Page.promote_panels + SEOMixin.seo_panels

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Get filter parameters from request
        sort_by = request.GET.get('sort_by', 'title')
        search_query = request.GET.get('search', '')

        # Start with all live activities
        activities = ActivityPage.objects.live()

        # Apply search filter if provided
        if search_query:
            activities = activities.filter(title__icontains=search_query)

        # Apply sorting
        if sort_by == 'latest':
            activities = activities.order_by('-first_published_at')
        else:  # Default to sorting by title
            activities = activities.order_by('title')

        # Pass all parameters to the template
        context['activities'] = activities
        context['sort_by'] = sort_by
        context['search_query'] = search_query

        return context

    class Meta:
        verbose_name = "Liste des Activités"