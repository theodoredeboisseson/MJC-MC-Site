from django.db import models
from django.forms.widgets import CheckboxSelectMultiple
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet

from apps.common.mixins import ContentMixin, VilleMixin
from apps.common.models import DetailPage, SEOMixin, BasePage


@register_snippet
class Animateur(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

@register_snippet
class ActivityCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie d'activité"
        verbose_name_plural = "Catégories d'activités"

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
    link = models.URLField(max_length=200, help_text="Lien de redirection pour le bouton", blank=True)
    categories = ParentalManyToManyField(
        'activites.ActivityCategory',
        blank=True,
        related_name='activities',
        help_text='Pour chercher par catégorie dans la liste des activités'
    )
    
    content_panels = DetailPage.content_panels + [
        FieldPanel('animateurs', widget=CheckboxSelectMultiple),
        InlinePanel('sub_activities', label="Sous Activités"),
        FieldPanel('link'),
        FieldPanel('categories', widget=CheckboxSelectMultiple),
    ]

    class Meta:
        verbose_name = "Activité"

class ActivityList(BasePage, ContentMixin):
    content_panels = BasePage.content_panels + ContentMixin.content_panels
    promote_panels = BasePage.promote_panels

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Get filter parameters from request
        sort_by = request.GET.get('sort_by', 'title')
        search_query = request.GET.get('search', '')
        category_id = request.GET.get('category', '')
        villes = request.GET.get('ville', '')

        # Start with all live activities
        activities = ActivityPage.objects.live()
    
        # Apply search filter if provided
        if search_query:
            activities = activities.filter(title__icontains=search_query)
    
        # Apply category filter if provided
        if category_id:
            activities = activities.filter(categories__id=category_id)
    
        # Apply sorting
        if sort_by == 'latest':
            activities = activities.order_by('-first_published_at')
        else:  # Default to sorting by title
            activities = activities.order_by('title')

        # Validate villes
        if villes:
            ville_list = villes.split(',')
            activities = activities.filter(ville__in=ville_list)
        else:
            ville_list = []
    
        # Ajouter les catégories au contexte
        context['activities'] = activities
        context['sort_by'] = sort_by
        context['villes'] = ville_list
        context['search_query'] = search_query
        context['categories'] = ActivityCategory.objects.all()
        context['selected_category'] = category_id
    
        return context

    class Meta:
        verbose_name = "Liste des Activités"