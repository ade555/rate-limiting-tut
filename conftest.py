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


@pytest.fixture
def user_access_token(user_payload, api_client) -> str:
    user = api_client.post('/api/users/signup/', data = user_payload, format="json")
    user_login = api_client.post('/api/users/login/', data={"email":"johndoe@email.com", "password":"testing123"})
    return user_login.data['access']

@pytest.fixture
def user_api_key(api_client, user_access_token)->str:
    headers = {'Authorization':f'Bearer {user_access_token}'}
    response = api_client.get('/api/users/api_key/get/', headers=headers)
    return response.data['data']['key']

@pytest.fixture
def book_payload()->dict:
    return {"title":"Tom and Jerry Book One"}