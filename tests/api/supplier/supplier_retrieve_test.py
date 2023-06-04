from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.serializers.contact_serializer import ContactSerializer
from api.serializers.supplier_serializer import SupplierSerializer
from tests.factories import ContactFactory, SupplierFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestSupplierRetrieveView:
    """Tests for supplier retrieve view"""

    @pytest.mark.django_db
    def test_supplier_retrieve(self, authenticated_user, user) -> None:
        """
        Test that authenticated user can get the supplier
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can get expected supplier
        Returns:
            None
        Raises:
            AssertionError
        """

        supplier = SupplierFactory(type=1)

        url: str = reverse('supplier-detail', kwargs={'pk': supplier.id})

        expected_response: Dict = SupplierSerializer(supplier).data
        response: Response = authenticated_user.get(url)

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data == expected_response, 'Неправильный участник'
