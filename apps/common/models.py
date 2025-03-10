from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.models import Page

from apps.common.mixins import SEOMixin, ContentMixin


class BasePage(Page, SEOMixin):
    """Base page class with SEO enhancements for all site pages."""

    # Add any fields that should be common to all pages

    # Add SEO panels to promote_panels
    promote_panels = Page.promote_panels + SEOMixin.seo_panels

    class Meta:
        abstract = True
        
        
class BaseIndexPage(BasePage):
    def get_context(self, request):
        context = super().get_context(request)
        context['subpages'] = self.get_children().live().order_by('title')
        return context

    class Meta:
        verbose_name = "Page d'index de base"


class DetailPage(BasePage, ContentMixin):
    subtitle = models.CharField(max_length=250, blank=True, verbose_name="Sous-titre")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Image"
    )

    content_panels = BasePage.content_panels + ContentMixin.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
    ]

    class Meta:
        verbose_name = "Page de détail"


@register_setting
class FooterSettings(ClusterableModel, BaseGenericSetting):
    school_schedule = RichTextField(
        verbose_name="Horaires période scolaire Mauguio",
        blank=True,
    )
    vacation_schedule = RichTextField(
        verbose_name="Horaires période vacances Mauguio",
        blank=True,
    )
    extra = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Message en extra Mauguio (optionnel)"
    )
    carnon_school_schedule = RichTextField(
        verbose_name="Horaires période scolaire Carnon",
        blank=True,
    )
    carnon_vacation_schedule = RichTextField(
        verbose_name="Horaires période vacances Carnon",
        blank=True,
    )
    carnon_extra = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Message en extra Carnon (optionnel)"
    )
    panels = [
        MultiFieldPanel([
            FieldPanel('school_schedule'),
            FieldPanel('vacation_schedule'),
            FieldPanel('extra'),
        ], heading="Mauguio"),
        MultiFieldPanel([
            FieldPanel('carnon_school_schedule'),
            FieldPanel('carnon_vacation_schedule'),
            FieldPanel('carnon_extra'),
        ], heading="Carnon"),
    ]

    class Meta:
        verbose_name = "Informations du Pied de page"


@register_setting
class FlashMessage(BaseGenericSetting):
    message = RichTextField(
        help_text="Jusqu'à 100 caractères",
        blank=True,
        null=True
    )
    show = models.BooleanField(
        verbose_name="Montrer",
        default=False
    )

    panels = [
        FieldPanel('message'),
        FieldPanel('show'),
    ]
    
    class Meta:
        verbose_name = "Message Flash"

    def __str__(self):
        return self.message[:100]