import json
from requests import get, post, put, delete
from rest_framework import status


users_url = 'http://127.0.0.1:8000/users/'
tasks_url = 'http://127.0.0.1:8000/tasks/'

data_user = {
                'name': 'Usuario teste',
                'email': 'teste@teste.com',
                'age': '21',
                'user_type': 'admin'
            }

data_task = {
                'descricao': 'Tarefa teste',
                'user_id': '1',
            }


def test_create_user_returning_201():

    request = post(users_url, json=data_user)

    assert request.status_code == status.HTTP_201_CREATED


def test_create_user_manager_returning_201():

    data = {
                'name': 'Usuario teste',
                'email': 'teste@teste.com',
                'age': '21',
                'user_type': 'manager'
            }

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_201_CREATED


def test_create_user_default_returning_201():

    data = {
                'name': 'Usuario teste',
                'email': 'teste@teste.com',
                'age': '21',
                'user_type': 'default'
            }

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_201_CREATED


def test_create_user_with_wrong_type_returning_400():

    data = {
                'name': 'Usuario do tipo errado',
                'email': 'teste@teste.com',
                'age': '21',
                'user_type': 'superuser'
            }

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user_with_age_smaller_18_returning_400():

    data = {
                'name': 'Usuario com 15 anos',
                'email': 'teste@teste.com',
                'age': '15',
                'user_type': 'admin'
            }

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user_with_lenght_name_higher_50_returning_400():

    data = {
            'name': 'Nome maior que 50 caracteres Nome maior que 50 caracte',
            'email': 'teste@teste.com',
            'age': '20',
            'user_type': 'admin'
            }

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_400_BAD_REQUEST


def test_create_user_with_wrong_email_returning_400():

    data = {
                'name': 'Usuario com email errado',
                'email': 'teste',
                'age': '20',
                'user_type': 'admin'
            }

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_400_BAD_REQUEST


def test_get_users_url_returning_200():

    request = get(users_url)

    assert request.status_code == status.HTTP_200_OK


def test_get_user_detail_url_returning_200():

    request = get(users_url + '1')

    assert request.status_code == status.HTTP_200_OK


def test_update_user_returning_200():

    json = {
        'name': 'Usuario teste atualizado',
        'email': 'teste@teste.com',
        'age': '21',
        'user_type': 'admin'
    }
    request = put(users_url + '1/', json=json)

    assert request.status_code == status.HTTP_200_OK


def test_delete_user_returning_204():

    post(users_url, json=data_user)
    req = get(users_url)

    users = json.loads(req.text)
    count = len(users['results']) - 1
    id = users['results'][count]['id']

    request = delete(users_url + str(id) + '/', json=data_user)

    assert request.status_code == status.HTTP_204_NO_CONTENT


def test_get_tasklist_by_user():
    req = post(tasks_url, json=data_task)

    request = get(users_url + '1/tasks')

    assert req.status_code == status.HTTP_201_CREATED
    assert request.status_code == status.HTTP_200_OK
