from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.serializers.product_serializer import ProductSerializer
from tests.factories import ProductFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestProductRetrieveView:
    """Tests for product retrieve view"""

    @pytest.mark.django_db
    def test_product_retrieve(self, authenticated_user, user) -> None:
        """
        Test that authenticated user can get the product
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can get expected product
        Returns:
            None
        Raises:
            AssertionError
        """

        product = ProductFactory()
        url: str = reverse('product-detail', kwargs={'pk': product.id})

        expected_response: Dict = ProductSerializer(product).data
        response: Response = authenticated_user.get(url)

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data == expected_response, 'Неправильный товар'
