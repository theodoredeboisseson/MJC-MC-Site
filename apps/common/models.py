from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.fields import RichTextField
from wagtail.models import Page
from colorfield.fields import ColorField

from apps.common.mixins import SEOMixin, ContentMixin


class BasePage(Page, SEOMixin):
    """Base page class with SEO enhancements for all site pages."""

    # Add any fields that should be common to all pages

    # Add SEO panels to promote_panels
    promote_panels = Page.promote_panels + SEOMixin.seo_panels

    class Meta:
        abstract = True


class BaseIndexPage(BasePage):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Image pour la liste",
        help_text="L'image sert de miniature si la page est affichée dans une liste"
    )
    
    content_panels = BasePage.content_panels + [
        FieldPanel('image'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        context['subpages'] = self.get_children().live().specific().order_by('title')
        return context

    class Meta:
        verbose_name = "Page liste des sous-pages"


class DetailPage(BasePage, ContentMixin):
    subtitle = models.CharField(max_length=250, blank=True, verbose_name="Sous-titre")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Image",
        help_text="L'image sert de miniature si la page est affichée dans une liste"
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


@register_setting(icon='cog')
class ThemeSettings(BaseGenericSetting):
    color_primary = ColorField(
        default="#20223B",
        verbose_name="Couleur primaire (en hexadécimal)",
        blank=True
    )
    color_secondary = ColorField(
        default="#297a62",
        verbose_name="Couleur secondaire (en hexadécimal)",
        blank=True
    )
    color_background = ColorField(
        default="#f0f4f8",
        verbose_name="Couleur d'arrière-plan (en hexadécimal)",
        blank=True
    )
    color_dark_text = ColorField(
        default="#20223B",
        verbose_name="Couleur du texte sombre (en hexadécimal)",
        blank=True
    )
    color_light_text = ColorField(
        default="#edf2f7",
        verbose_name="Couleur du texte clair (en hexadécimal)",
        blank=True
    )
    color_link_hover = ColorField(
        default="#63b3ed",
        verbose_name="Couleur au survol des liens (en hexadécimal)",
        blank=True
    )
    color_section_bg = ColorField(
        default="#d7e8ef",
        verbose_name="Couleur de fond des sections (en hexadécimal)",
        blank=True
    )

    panels = [
        FieldPanel("color_primary"),
        FieldPanel("color_secondary"),
        FieldPanel("color_background"),
        FieldPanel("color_dark_text"),
        FieldPanel("color_light_text"),
        FieldPanel("color_link_hover"),
        FieldPanel("color_section_bg"),
    ]
    
    class Meta:
        verbose_name = "Thème de couleurs"