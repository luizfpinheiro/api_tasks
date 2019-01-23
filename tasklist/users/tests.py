import pytest
from requests import get
from rest_framework import status

users_url = 'http://127.0.0.1:8000/users/'
tasks_url = 'http://127.0.0.1:8000/tasks/'


def test_users_url_returning_200():

    request = get(users_url)
    
    assert request.status_code == status.HTTP_200_OK
    

def test_users_detail_url_returning_200():

    request = get(users_url + '1')

    assert request.status_code == status.HTTP_200_OK