from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

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
    # path("api/auth/", include("rest_framework.urls")),  # REST Framework autentifikatsiyasi
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Access va Refresh token olish uchun
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Refresh token yordamida yangi Access token olish uchun
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)