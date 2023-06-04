from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns: list = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path("core/", include("core.urls")),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
