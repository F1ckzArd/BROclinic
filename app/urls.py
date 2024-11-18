
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls", namespace="main")),
    path("", include("authentication.urls", namespace="authentication")),
    path("", include("docs.urls", namespace="docs")),
    path("", include("articles.urls", namespace="articles")),
    path('martor/', include('martor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
