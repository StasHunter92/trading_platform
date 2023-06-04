import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from tests.factories import ContactFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestContactDestroyView:
    """Tests for contact destroy view"""

    @pytest.mark.django_db
    def test_contact_delete(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can delete the contact
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 204
            - User can delete the contact
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()

        url: str = reverse('contact-detail', kwargs={'pk': contact.id})

        response: Response = authenticated_user.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT, 'Контакт не удален'
