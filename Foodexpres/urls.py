from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("user_app.urls")),  # Ilova URL larini bog'lash
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),  # API sxemasi
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),  # API dokumentatsiyasi uchun Swagger UI
    path("api/auth/", include("rest_framework.urls")),  # REST Framework autentifikatsiyasi
    path("api/token/", include("dj_rest_auth.urls")),  # JWT autentifikatsiyasi uchun
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)