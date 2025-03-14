from wagtail.models import Page

def page_keywords(request):
    """Build dynamic keywords based on page hierarchy"""
    base_keywords = "MJC, Maison des Jeunes et de la Culture, Mauguio Carnon"
#    MJC Maison des Jeunes et de la Culture, MJC, Maison des Jeunes et de la Culture, {{ page.title }}, Mauguio Carnon, Mauguio, Carnon, Mauguio-Carnon, évènements, activités, association, gala, danse, sport, chant, musique, muscu, gymnastique, melgeil, e-sport, jeunes, enfants, famille, retraités #}

    # Récupérer la page actuelle, si présente dans la requête ou via find_for_request
    page = getattr(request, 'page', Page.find_for_request(request, request.path))

    if not page:
        return {'dynamic_keywords': base_keywords}

    # Collecter les mots-clés des pages parentes
    parent_keywords = ", ".join(
        parent.specific.seo_keywords for parent in page.get_ancestors() if hasattr(parent.specific, 'seo_keywords') and parent.specific.seo_keywords
    )

    specific_keywords = getattr(page.specific, 'seo_keywords', '')
    all_keywords = [base_keywords, parent_keywords, specific_keywords, page.title]

    dynamic_keywords = ", ".join(filter(None, all_keywords))

    return {'dynamic_keywords': dynamic_keywords}
