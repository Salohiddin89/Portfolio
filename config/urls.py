from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from portfolio import views
from portfolio.sitemaps import StaticViewSitemap, ProjectSitemap, BlogSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "projects": ProjectSitemap,
    "blogs": BlogSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/send-message/", views.send_message, name="send_message"),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]

urlpatterns += i18n_patterns(
    path("", views.home, name="home"),
    path("project/<int:pk>/", views.project_detail, name="project_detail"),
    path("blog/<int:pk>/", views.blog_detail, name="blog_detail"),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
