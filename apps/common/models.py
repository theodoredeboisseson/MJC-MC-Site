from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page

class SEOMixin(models.Model):
    seo_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated keywords specific to this page"
    )

    seo_panels = [
        MultiFieldPanel([
            FieldPanel('seo_keywords'),
        ], heading="SEO Keywords"),
    ]

    class Meta:
        abstract = True


class BasePage(Page, SEOMixin):
    """Base page class with SEO enhancements for all site pages."""

    # Add any fields that should be common to all pages

    # Add SEO panels to promote_panels
    promote_panels = Page.promote_panels + SEOMixin.seo_panels

    class Meta:
        abstract = True

class DetailPage(BasePage):
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