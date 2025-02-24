from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class AssociationIndexPage(Page):
    content = RichTextField(blank=True, verbose_name="Contenu")

    content_panels = Page.content_panels + [
        FieldPanel('content'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['subpages'] = AssociationPage.objects.child_of(self).live().order_by('title')
        return context

    subpage_types = ['association.AssociationPage']
    
    class Meta:
        verbose_name = "Grille pages de l'Association"
        
class AssociationPage(Page):
    template = 'association/association_page.html'
    subtitle = models.CharField(max_length=250, blank=True, verbose_name="Sous-titre")
    body = RichTextField(verbose_name="Contenu")
    card_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Cette image sera utilisée pour la vignette dans la page d'index",
        verbose_name="Image"
    )
    show_image_in_page = models.BooleanField(
        default=True,
        verbose_name="Afficher l'image dans la page",
        help_text="Décochez pour afficher l'image uniquement dans la grille de la page parente"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('card_image'),
            FieldPanel('show_image_in_page'),
        ], heading="Image de la page"),
        FieldPanel('subtitle'),
        FieldPanel('body'),
    ]

    parent_page_types = ['association.AssociationIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = "Page de l'Association"