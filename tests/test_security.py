from http import HTTPStatus

import pytest
from fastapi import HTTPException
from jwt import decode

from fast_zero.models import User
from fast_zero.security import create_access_token, get_current_user, settings


def test_jwt():
    data = {'sub': 'test@test.com'}
    token = create_access_token(data)

    result = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert result['sub'] == data['sub']
    assert result['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}


def test_get_current_user_missing_username(session, user):
    token = create_access_token(data={'bub': user.email})

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(session, token)

    assert exc_info.value.status_code == HTTPStatus.UNAUTHORIZED


def test_get_current_user_user_not_found(session):
    user_fake = User(username='duca', email='duca@test.com', password='test')
    token = create_access_token(data={'sub': user_fake.email})

    with pytest.raises(HTTPException) as exc_info:
        get_current_user(session, token)

    assert exc_info.value.status_code == HTTPStatus.UNAUTHORIZED
