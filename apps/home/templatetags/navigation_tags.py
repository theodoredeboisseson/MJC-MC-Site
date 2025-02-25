from django import template

from wagtail.models import Site

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

@register.simple_tag
def get_parent_url(page):
    parent = page.get_parent()
    return parent.url if parent else '/'