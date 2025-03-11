from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.template.response import TemplateResponse
from wagtail.contrib.search_promotions.models import Query
from wagtail.search.backends import get_search_backend
from wagtail.models import Page
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity

def search(request):
    search_query = request.GET.get("query", "").strip()
    page_number = request.GET.get("page", 1)

    # Vérifier si la requête est vide
    if not search_query:
        return TemplateResponse(
            request,
            "search/search.html",
            {
                "search_query": "",
                "search_results": Page.objects.none(),
            },
        )

    # Recherche principale avec Wagtail
    search_results = Page.objects.live().annotate(
        similarity=TrigramSimilarity("title", search_query) + TrigramSimilarity("search_description", search_query),
        rank=SearchRank(SearchVector("title", weight="A") + SearchVector("search_description", weight="B"), SearchQuery(search_query)),
    ).filter(
        Q(title__icontains=search_query) |
        Q(search_description__icontains=search_query) |
        Q(similarity__gt=0.1)  # Ajustable pour plus ou moins de tolérance
    ).order_by("-rank", "-similarity")

    # Enregistrement de la requête pour l'analyse des recherches (facultatif)
    if search_results.exists():
        query = Query.get(search_query)
        query.add_hit()

    # Pagination
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        search_results = paginator.page(1)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
