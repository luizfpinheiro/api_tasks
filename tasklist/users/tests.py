import pytest
from requests import get, post, put, delete
from rest_framework import status

users_url = 'http://127.0.0.1:8000/users/'
tasks_url = 'http://127.0.0.1:8000/tasks/'
data = {
        'name': 'Usuario teste',
        'email': 'teste@teste.com',
        'age': '21',
        'user_type': 'admin'
    }

    
def test_create_user__returning_201():

    request = post(users_url, json=data)

    assert request.status_code == status.HTTP_201_CREATED

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
    request = put(users_url + '1/' , json=json)

    assert request.status_code == status.HTTP_200_OK


# def test_delete_user():
    
#     post(users_url, json=data)
#     count = User.objects.count
#     request = delete(users_url + str(count) + '/', json=data)

#     assert request.status_code == status.HTTP_204_NO_CONTENT
