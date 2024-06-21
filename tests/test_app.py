from http import HTTPStatus


def test_root_deve_retorna_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'testpassword',
            'email': 'test@email.com',
        },
    )

    # voltou os dados corretos
    assert response.status_code == HTTPStatus.CREATED
    # Validar o UserPublic
    assert response.json() == {
        'username': 'testusername',
        'email': 'test@email.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'username': 'testusername', 'email': 'test@email.com', 'id': 1}
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test2username',
            'email': 'test2@email.com',
            'password': 'testpassword',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'test2username',
        'email': 'test2@email.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted successfully'}
