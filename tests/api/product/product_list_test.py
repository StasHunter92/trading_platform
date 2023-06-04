from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.serializers.product_serializer import ProductSerializer
from tests.factories import ProductFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestProductListView:
    """Tests for product list view"""

    url: str = reverse('product-list')

    @pytest.mark.django_db
    def test_product_list(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can get a list of products
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can get expected product list
        Returns:
            None
        Raises:
            AssertionError
        """

        products = ProductFactory.create_batch(size=5)

        expected_response: Dict = ProductSerializer(
            products,
            many=True
        ).data

        response: Response = authenticated_user.get(self.url)

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data == expected_response, 'Списки товаров не совпадают'
