from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.product_model import Product
from tests.factories import ProductFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestProductUpdateView:
    """Tests for product update view"""

    @pytest.mark.django_db
    def test_product_update(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can update the product
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can update the product
            - Updated product exists in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        product = ProductFactory()
        url: str = reverse('product-detail', kwargs={'pk': product.id})

        update_data: Dict[str, str] = {
            'title': 'New product title',
            'model': 'new model',
            'release_date': '2000-12-12'
        }

        response: Response = authenticated_user.put(url, data=update_data)
        updated_product = Product.objects.filter(
            title=update_data['title'],
            model=update_data['model'],
            release_date=update_data['release_date'],
        ).exists()

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data['title'] == update_data['title'], 'Обновленные данные не совпадают'
        assert updated_product, 'Товар не обновлен'
