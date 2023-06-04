from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.supplier_model import Supplier
from tests.factories import ContactFactory, ProductFactory, SupplierFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestSupplierCreateView:
    """Tests for supplier create view"""

    url: str = reverse('supplier-list')

    @pytest.mark.django_db
    def test_supplier_create(self, authenticated_user, user) -> None:
        """
        Test to check if a new supplier can be created successfully
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 201
            - Created supplier exists in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()
        products = ProductFactory.create_batch(size=5)

        create_data: Dict[str, str] = {
            'type': 1,
            'title': 'Apple',
            'contact': contact.pk,
            'products': [product.pk for product in products]
        }

        response: Response = authenticated_user.post(self.url, data=create_data)

        created_supplier = Supplier.objects.filter(
            title=create_data['title'],
        ).exists()

        assert response.status_code == status.HTTP_201_CREATED, 'Участник не создан'
        assert created_supplier, 'Созданного участника не существует'

    # -------------------------------------------------------------------------
    @pytest.mark.django_db
    def test_supplier_create_fail(self, authenticated_user, user) -> None:
        """
        Test to check if a new supplier can not be created with nested_supplier if it's type is Factory
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 400
            - Created supplier does not exist in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()
        nested_supplier = SupplierFactory(type=1)

        create_data: Dict[str, str] = {
            'type': 1,
            'title': 'Apple',
            'contact': contact.pk,
            'supplier': nested_supplier.pk
        }

        response: Response = authenticated_user.post(self.url, data=create_data)
        created_supplier = Supplier.objects.filter(
            title=create_data['title'],
        ).exists()

        assert response.status_code == status.HTTP_400_BAD_REQUEST, 'Участник создан'
        assert response.data['non_field_errors'][0] == 'Factory does not have a supplier', 'Вы добавили поставщика'
        assert not created_supplier, 'Созданный участник существует'

    # -------------------------------------------------------------------------
    @pytest.mark.django_db
    def test_contact_deny(self, api_client) -> None:
        """
        Test that unauthenticated users cannot access the supplier create API endpoint
        Args:
            api_client: API client without user for testing
        Checks:
            - Response status code is 403
        Returns:
            None
        Raises:
            AssertionError
        """

        response: Response = api_client.post(self.url)

        assert response.status_code == status.HTTP_403_FORBIDDEN, 'Отказ в доступе не предоставлен'
