from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.serializers.contact_serializer import ContactSerializer
from tests.factories import ContactFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestContactListView:
    """Tests for contact list view"""

    url: str = reverse('contact-list')

    @pytest.mark.django_db
    def test_contact_list(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can get a list of contacts
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can get expected contact list
        Returns:
            None
        Raises:
            AssertionError
        """

        contacts = ContactFactory.create_batch(size=5)

        expected_response: Dict = ContactSerializer(
            contacts,
            many=True
        ).data

        response: Response = authenticated_user.get(self.url)

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data == expected_response, 'Списки контактов не совпадают'
