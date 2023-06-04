from typing import Dict

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response

from api.models.contact_model import Contact
from tests.factories import ContactFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create tests
class TestContactUpdateView:
    """Tests for contact update view"""

    @pytest.mark.django_db
    def test_contact_update(self, authenticated_user, user) -> None:
        """
        Test to check that authenticated user can update the contact
        Args:
            authenticated_user: API client with authenticated user for testing
            user: A fixture that creates a user instance
        Checks:
            - Response status code is 200
            - User can update the contact
            - Updated contact exists in the database
        Returns:
            None
        Raises:
            AssertionError
        """

        contact = ContactFactory()
        url: str = reverse('contact-detail', kwargs={'pk': contact.id})

        update_data: Dict[str, str] = {
            'email': 'test@example.com',
            'country': 'Россия',
            'city': 'Санкт-Петербург',
            'street_name': 'Тестовая',
            'building_number': '123',
        }

        response: Response = authenticated_user.put(url, data=update_data)
        updated_contact = Contact.objects.filter(
            email=update_data['email'],
            country=update_data['country'],
            city=update_data['city'],
            street_name=update_data['street_name'],
            building_number=update_data['building_number'],
        ).exists()

        assert response.status_code == status.HTTP_200_OK, 'Запрос не прошел'
        assert response.data['email'] == update_data['email'], 'Обновленные данные не совпадают'
        assert updated_contact, 'Контакт не обновлен'
