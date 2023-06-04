from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.supplier_model import Supplier
from tests.factories import ContactFactory, SupplierFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestSupplierUpdateView:
    """Tests for supplier update view"""

    @pytest.mark.django_db
    def test_supplier_update(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can update the supplier
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can update the supplier
            - Updated supplier exists in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()
        supplier = SupplierFactory(type=2, indebtedness=100)

        url: str = reverse('supplier-detail', kwargs={'pk': supplier.id})

        update_data: Dict[str, str] = {
            'type': 3,
            'title': 'New title',
            'contact': contact.pk,
            'indebtedness': 200,
        }

        response: Response = authenticated_user.put(url, data=update_data)

        updated_supplier = Supplier.objects.filter(
            type=update_data['type'],
            title=update_data['title'],
            contact=update_data['contact'],
        ).exists()
        supplier.refresh_from_db()

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data['contact'] == update_data['contact'], 'Обновленные данные не совпадают'
        assert updated_supplier, 'Участник не обновлен'
        assert supplier.indebtedness != update_data['indebtedness'], 'Задолженность изменена'
