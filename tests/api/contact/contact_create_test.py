from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.contact_model import Contact


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestContactCreateView:
    """Tests for contact create view"""

    url: str = reverse('contact-list')

    @pytest.mark.django_db
    def test_contact_create(self, authenticated_user, user) -> None:
        """
        Test to check if a new contact can be created successfully
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 201
            - Created contact exists in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        create_data: Dict[str, str] = {
            'email': 'test@example.com',
            'country': 'Россия',
            'city': 'Санкт-Петербург',
            'street_name': 'Тестовая',
            'building_number': '123',
        }

        response: Response = authenticated_user.post(self.url, data=create_data)
        created_contact = Contact.objects.filter(
            email=create_data['email'],
        ).exists()

        assert response.status_code == status.HTTP_201_CREATED, 'Контакт не создан'
        assert created_contact, 'Созданного контакта не существует'

    # -------------------------------------------------------------------------
    @pytest.mark.django_db
    def test_contact_deny(self, api_client) -> None:
        """
        Test that unauthenticated users cannot access the contact create API endpoint
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
