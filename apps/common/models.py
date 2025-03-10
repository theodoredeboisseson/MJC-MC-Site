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
        abstract = True


@register_setting
class FooterSettings(ClusterableModel, BaseGenericSetting):
    school_hours_content = RichTextField(
        verbose_name="Horaires période scolaire",
        blank=True,
    )
    vacation_hours_content = RichTextField(
        verbose_name="Horaires période vacances",
        blank=True,
    )
    extra = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Message en extra (optionnel)"
    )
    panels = [
        FieldPanel('school_hours_content'),
        FieldPanel('vacation_hours_content'),
        FieldPanel('extra'),
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