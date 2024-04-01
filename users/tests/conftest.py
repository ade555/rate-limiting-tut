import pytest
from rest_framework.test import APIClient
from users.models import User


@pytest.fixture
def api_client() -> APIClient:  
    """  
    Fixture to provide an API client  
    """  
    yield APIClient()


@pytest.fixture
def user_payload() -> dict:
    return {
    "first_name":"john",
    "last_name":"doe",
    "username":"john",
    "email":"johndoe@email.com",
    "password":"testing123"
}

