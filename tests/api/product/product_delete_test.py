import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from tests.factories import ProductFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestProductDestroyView:
    """Tests for product destroy view"""

    @pytest.mark.django_db
    def test_product_delete(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can delete the product
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 204
            - User can delete the product
        Returns:
            None
        Raises:
            AssertionError
        """

        product = ProductFactory()

        url: str = reverse('product-detail', kwargs={'pk': product.id})

        response: Response = authenticated_user.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT, 'Товар не удален'
