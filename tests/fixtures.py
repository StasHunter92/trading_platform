import pytest
from rest_framework.test import APIClient

from tests.factories import UserFactory


# ----------------------------------------------------------------------------------------------------------------------
# Create fixtures
@pytest.fixture
def api_client() -> APIClient:
    """A fixture that creates an instance of the APIClient"""
    return APIClient()


@pytest.fixture
def user():
    """A fixture that creates a user instance"""
    return UserFactory.create(username="username", password="testp@ssword")


@pytest.fixture
def authenticated_user(api_client, user) -> APIClient:
    """A fixture that creates authenticated user on the APIClient"""
    api_client.force_authenticate(user=user)
    return api_client
