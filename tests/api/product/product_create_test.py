from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.product_model import Product


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestProductCreateView:
    """Tests for product create view"""

    url: str = reverse('product-list')

    @pytest.mark.django_db
    def test_product_create(self, authenticated_user, user) -> None:
        """
        Test to check if a new product can be created successfully
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 201
            - Created product exists in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        create_data: Dict[str, str] = {
            'title': 'iPhone',
            'model': '14 Pro Max',
            'release_date': '2023-09-16',
        }

        response: Response = authenticated_user.post(self.url, data=create_data)
        created_product = Product.objects.filter(
            title=create_data['title'],
            model=create_data['model']
        ).exists()

        assert response.status_code == status.HTTP_201_CREATED, 'Товар не создан'
        assert created_product, 'Созданного товара не существует'

    # -------------------------------------------------------------------------
    @pytest.mark.django_db
    def test_product_deny(self, api_client) -> None:
        """
        Test that unauthenticated users cannot access the product create API endpoint
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
