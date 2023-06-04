from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.serializers.supplier_serializer import SupplierSerializer
from tests.factories import SupplierFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestSupplierListView:
    """Tests for supplier list view"""

    url: str = reverse('supplier-list')

    @pytest.mark.django_db
    def test_supplier_list(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can get a list of suppliers
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can get expected supplier list
        Returns:
            None
        Raises:
            AssertionError
        """

        suppliers = SupplierFactory.create_batch(size=3, type=1)

        expected_response: Dict = SupplierSerializer(
            suppliers,
            many=True
        ).data

        response: Response = authenticated_user.get(self.url)

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data == expected_response, 'Списки участников не совпадают'
