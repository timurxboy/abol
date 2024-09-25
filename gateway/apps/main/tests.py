import pytest
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
from django.urls import reverse
from unittest.mock import patch
import grpc


class CustomRpcError(grpc.RpcError):
    def __init__(self, details, code):
        self._details = details
        self._code = code

    def code(self):
        return self._code

    def details(self):
        return self._details


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpass')


@pytest.fixture
def jwt_token(user):
    return AccessToken.for_user(user)


@pytest.mark.django_db
@patch('grpc_client.list_book')
def test_get_list_book_success(mock_list_book, api_client, jwt_token):
    mock_list_book.return_value = type('Response', (object,), {
        'data': [
            type('Book', (object,), {
                'id': 1,
                'name': 'Test Book',
                'author': 'Author Name',
                'publication_date': '2023-01-01'
            })()
        ]
    })

    response = api_client.get(
        reverse('Book', args=[]),
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}'
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == [{
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    }]


@pytest.mark.django_db
@patch('grpc_client.get_book')
def test_get_book_success(mock_get_book, api_client, jwt_token):
    mock_get_book.return_value = type('Book', (object,), {
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    })()

    response = api_client.get(
        reverse('Book-Detail', args=[1]),
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}'
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    }


@pytest.mark.django_db
@patch('grpc_client.get_book')
def test_get_book_not_found(mock_get_book, api_client, jwt_token):
    mock_get_book.side_effect = CustomRpcError("Book with ID 999 not found.", grpc.StatusCode.NOT_FOUND)

    response = api_client.get(
        reverse('Book-Detail', args=[999]),
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}'
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.data == "Book with ID 999 not found."


@pytest.mark.django_db
@patch('grpc_client.get_book')
def test_get_book_internal_server_error(mock_get_book, api_client, jwt_token):
    mock_get_book.side_effect = CustomRpcError("Internal error.", grpc.StatusCode.INTERNAL)

    response = api_client.get(
        reverse('Book-Detail', args=[1]),
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}'
    )

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


@pytest.mark.django_db
@patch('grpc_client.create_book')
def test_post_book_success(mock_create_book, api_client, jwt_token):
    mock_create_book.return_value = type('Book', (object,), {
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    })()

    response = api_client.post(
        reverse('Book', args=[]),
        data={
            'name': 'Test Book',
            'author': 'Author Name',
            'publication_date': '2023-01-01'
        },
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}',
        format='json'
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == {
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    }


@pytest.mark.django_db
@patch('grpc_client.update_book')
def test_put_book_success(mock_update_book, api_client, jwt_token):
    mock_update_book.return_value = type('Book', (object,), {
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    })()

    response = api_client.put(
        reverse('Book-Detail', args=[1]),
        data={
            'name': 'Test Book',
            'author': 'Author Name',
            'publication_date': '2023-01-01'
        },
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}',
        format='json'
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        'id': 1,
        'name': 'Test Book',
        'author': 'Author Name',
        'publication_date': '2023-01-01'
    }


@pytest.mark.django_db
@patch('grpc_client.update_book')
def test_put_book_not_found(mock_update_book, api_client, jwt_token):
    mock_update_book.side_effect = CustomRpcError("Book with ID 999 not found.", grpc.StatusCode.NOT_FOUND)

    response = api_client.put(
        reverse('Book-Detail', args=[999]),
        data={
            'name': 'Test Book',
            'author': 'Author Name',
            'publication_date': '2023-01-01'
        },
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}',
        format='json'
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
@patch('grpc_client.update_book')
def test_put_book_server_error(mock_update_book, api_client, jwt_token):
    mock_update_book.side_effect = CustomRpcError("Internal error.", grpc.StatusCode.INTERNAL)

    response = api_client.put(
        reverse('Book-Detail', args=[1]),
        data={
            'name': 'Test Book',
            'author': 'Author Name',
            'publication_date': '2023-01-01'
        },
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}',
        format='json'
    )

    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


@pytest.mark.django_db
@patch('grpc_client.delete_book')
def test_delete_book_success(mock_delete_book, api_client, jwt_token):
    mock_delete_book.return_value = None  # Успешное удаление ничего не возвращает

    response = api_client.delete(
        reverse('Book-Detail', args=[1]),
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}'
    )

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
@patch('grpc_client.delete_book')
def test_delete_book_not_found(mock_delete_book, api_client, jwt_token):
    mock_delete_book.side_effect = CustomRpcError("Book with ID 999 not found.", grpc.StatusCode.NOT_FOUND)

    response = api_client.delete(
        reverse('Book-Detail', args=[999]),
        HTTP_AUTHORIZATION=f'Bearer {jwt_token}'
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
