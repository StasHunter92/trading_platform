import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.contact_model import Contact
from api.models.product_model import Product
from api.models.supplier_model import Supplier
from tests.factories import ContactFactory, SupplierFactory, ProductFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestSupplierDestroyView:
    """Tests for supplier destroy view"""

    @pytest.mark.django_db
    def test_supplier_delete(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can delete the supplier
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 204
            - User can delete the supplier
            - Contact is not deleted
            - Product is not deleted
            - Nested supplier is not deleted
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()
        nested_supplier = SupplierFactory(type=1)
        product = ProductFactory()
        supplier = SupplierFactory(type=2, contact=contact, supplier=nested_supplier)
        supplier.products.add(product)

        url: str = reverse('supplier-detail', kwargs={'pk': supplier.id})

        response: Response = authenticated_user.delete(url)

        contact.refresh_from_db()
        product.refresh_from_db()
        nested_supplier.refresh_from_db()

        expected_contact = Contact.objects.filter(pk=contact.pk).exists()
        expected_nested_supplier = Supplier.objects.filter(pk=nested_supplier.pk).exists()
        expected_product = Product.objects.filter(pk=product.pk).exists()

        assert response.status_code == status.HTTP_204_NO_CONTENT, 'Участник не удален'
        assert expected_contact, 'Контакт удален'
        assert expected_product, 'Продукт удален'
        assert expected_nested_supplier, 'Поставщик удален'
