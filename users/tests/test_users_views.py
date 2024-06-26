import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_signup(api_client, user_payload):
    # send a good request body
    user = api_client.post('/api/users/signup/', data = user_payload, format="json")
    assert user.status_code == 201
    assert user.data['data']['first_name']==user_payload['first_name']

    # create user with the same credentials
    user2 = api_client.post('/api/users/signup/', data = user_payload, format="json")
    assert user2.status_code == 400
    assert user2.data['info']['email']==['user with this email already exists.']

    # send a bad request body
    del user_payload['first_name']
    response_create = api_client.post('/api/users/signup/', data = user_payload, format="json")
    assert response_create.status_code == 400
    assert response_create.data['message']=='failed'


@pytest.mark.django_db
def test_api_key_view(api_client, user_access_token):
    headers = {'Authorization':f'Bearer {user_access_token}'}
    response = api_client.get('/api/users/api_key/get/', headers=headers)
    assert response.status_code == 200

    # regenerate api key
    response = api_client.put('/api/users/api_key/get/', headers=headers)
    assert response.status_code == 200