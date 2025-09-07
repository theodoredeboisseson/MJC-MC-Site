
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from apps.search import views as search_views
from apps.home import views as home_views
from apps.common.wagtail_sitemap import WagtailPageSitemap

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path("sitemap/", home_views.sitemap, name="sitemap"),
    path("sitemap.xml", sitemap, {"sitemaps": {"wagtail": WagtailPageSitemap()}}, name="sitemap.xml"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [path("", include(wagtail_urls))]