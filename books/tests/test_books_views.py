import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_book_list_create_view(api_client, user_api_key, book_payload):
    # create new books
    headers = {'Authorization':user_api_key}

    response = api_client.post('/api/books/', data=book_payload, headers=headers)
    assert response.status_code == 201
    assert response.data['data']['title']==book_payload['title']
    logger.info(response.data)

    response = api_client.get('/api/books/', headers=headers)
    assert response.status_code == 200
    assert response.data['data'][0]['title']==book_payload['title']