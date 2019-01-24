import json
from requests import get, post, put, delete
from rest_framework import status


tasks_url = 'http://127.0.0.1:8000/tasks/'

data_task = {
                'descricao': 'Tarefa teste',
                'user_id': '1',
            }


def test_create_task__returning_201():

    request = post(tasks_url, json=data_task)

    assert request.status_code == status.HTTP_201_CREATED


def test_get_tasks_returning_200():

    request = get(tasks_url)

    assert request.status_code == status.HTTP_200_OK


def test_get_task_detail_url_returning_200():

    request = get(tasks_url + '1')

    assert request.status_code == status.HTTP_200_OK


def test_update_task_returning_200():

    json = {
                'descricao': 'Tarefa teste atualizada',
                'user_id': '1',
            }
    request = put(tasks_url + '1/', json=json)

    assert request.status_code == status.HTTP_200_OK


def test_delete_task_returning_204():

    post(tasks_url, json=data_task)
    req = get(tasks_url)

    tasks = json.loads(req.text)
    count = len(tasks['results']) - 1
    id = tasks['results'][count]['id']

    request = delete(tasks_url + str(id) + '/', json=data_task)

    assert request.status_code == status.HTTP_204_NO_CONTENT
