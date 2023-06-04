from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.serializers.contact_serializer import ContactSerializer
from tests.factories import ContactFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestContactRetrieveView:
    """Tests for contact retrieve view"""

    @pytest.mark.django_db
    def test_contact_retrieve(self, authenticated_user, user) -> None:
        """
        Test that authenticated user can get the contact
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can get expected contact
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()
        url: str = reverse('contact-detail', kwargs={'pk': contact.id})

        expected_response: Dict = ContactSerializer(contact).data
        response: Response = authenticated_user.get(url)

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data == expected_response, 'Неправильный контакт'
