from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.filters import CountryFilter
from api.models.contact_model import Contact
from api.models.product_model import Product
from api.models.supplier_model import Supplier
from api.serializers.contact_serializer import ContactSerializer
from api.serializers.product_serializer import ProductSerializer
from api.serializers.supplier_serializer import SupplierCreateSerializer, SupplierUpdateSerializer, SupplierSerializer


# ----------------------------------------------------------------------------------------------------------------------
# Create views
@extend_schema(tags=['Товары'])
@extend_schema_view(
    list=extend_schema(summary='Список всех товаров'),
    retrieve=extend_schema(summary='Товар'),
    create=extend_schema(summary='Добавить товар'),
    update=extend_schema(summary='Отредактировать товар'),
    destroy=extend_schema(summary='Удалить товар')
)
class ProductViewSet(viewsets.ModelViewSet):
    """ViewSet for the product"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes: tuple = (IsAuthenticated,)

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


# -----------------------------------------------------------------------------
@extend_schema(tags=['Контакты'])
@extend_schema_view(
    list=extend_schema(summary='Список всех контактов'),
    retrieve=extend_schema(summary='Контакт'),
    create=extend_schema(summary='Добавить контакт'),
    update=extend_schema(summary='Отредактировать контакт'),
    destroy=extend_schema(summary='Удалить контакт')
)
class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet for the contact"""

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes: tuple = (IsAuthenticated,)

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


# -----------------------------------------------------------------------------
@extend_schema(tags=['Участники'])
@extend_schema_view(
    list=extend_schema(summary='Список всех участников'),
    retrieve=extend_schema(summary='Участник'),
    create=extend_schema(summary='Добавить участника'),
    update=extend_schema(summary='Отредактировать участника'),
    destroy=extend_schema(summary='Удалить участника')
)
class SupplierViewSet(viewsets.ModelViewSet):
    """ViewSet for the supplier"""

    queryset = Supplier.objects.all()
    permission_classes: tuple = (IsAuthenticated,)
    filter_backends: tuple = (DjangoFilterBackend,)
    filterset_class = CountryFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return SupplierCreateSerializer
        elif self.action == 'update':
            return SupplierUpdateSerializer
        else:
            return SupplierSerializer

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
