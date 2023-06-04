from django.urls import path, include
from rest_framework import routers

from api.views import ProductViewSet, SupplierViewSet, ContactViewSet

# ----------------------------------------------------------------------------------------------------------------------
# Create api app urls
router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'contact', ContactViewSet)

urlpatterns: list = [
    path("", include(router.urls)),
]
