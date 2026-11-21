import requests
import pytest


url = "http://objapi.course.qa-practice.com/object"


#
# @pytest.fixture
# def mid():
#     print('medium')
#
# @pytest.fixture
# def crit():
#     print('critical')
#

@pytest.fixture(autouse=True)
def all_start():
    print("before test")
    yield
    print("after test")


@pytest.fixture(scope='session',autouse=True)
def start():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture()
def new_object():
    body = {
        "name": "Test Object",
        "data": {
            "color": "black",
            "size": "big"
        }
    }

    response = requests.post(url, json=body)
    assert response.status_code == 200, 'Status code is incorrect'
    post_id = response.json()['id']
    yield post_id
    requests.delete(f'{url}/{post_id}')


def test_get_object(all_start):
    response = requests.get(f'{url}/1')
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['id'] == 1, 'id is incorrect'

@pytest.mark.parametrize('name, color, size', [
    ('Test Object', 'black', 'big'),
    ('Phone', 'white', 'small'),
    ('Book', 'blue', 'medium')
])

def test_post_object_test(name, color, size):
    body = {
        "name": name,
        "data": {
            "color": color,
            "size": size
        }
    }
    response = requests.post(url, json=body)

    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == body['name']

    requests.delete(f'{url}/{response.json()["id"]}')

@pytest.mark.medium
def test_put_object_test(new_object):
    body = {
        "name": "Test Object 2",
        "data": {
            "color": "grey",
            "size": "small"
        }
    }
    response = requests.put(f'{url}/{new_object}', json=body).json()

    assert response['name'] == body['name']


def test_patch_object_test(new_object):
    body = {
        "name": "Test Object 335"
    }
    response = requests.patch(f'{url}/{new_object}', json=body).json()

    assert response['name'] == body['name']



@pytest.mark.critical
def test_delete_object_test(new_object):
    response = requests.delete(f'{url}/{new_object}')

    assert response.status_code == 200


def test_get_object_test(new_object):
    response = requests.get(f'{url}/{new_object}')

    assert response.status_code == 200
    assert response.json()['id'] == new_object


