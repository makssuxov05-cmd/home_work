
import requests

url = "https://objapi.course.qa-practice.com/object"


def get_object(id_obj):
    res = requests.get(f'{url}/{id_obj}')
    return res.json()


def post_new_object():
    data = {
        "name": "Test Object",
        "data": {
            "color": "black",
            "size": "big"
        }
    }

    res = requests.post(url, json=data)
    assert res.status_code == 200
    return res.json()['id']


def delete_object(id_obj):
    res = requests.delete(f'{url}/{id_obj}')
    assert res.status_code == 200


def post_object_test():
    data = {
        "name": "Test Object",
        "data": {
            "color": "black",
            "size": "big"
        }
    }

    res = requests.post(url, json=data)

    assert res.status_code == 200
    assert res.json()['name'] == data['name']

    delete_object(res.json()['id'])


def put_object_test():
    id_obj = post_new_object()

    data = {
        "name": "Test Object 2",
        "data": {
            "color": "grey",
            "size": "small"
        }
    }

    res = requests.put(f'{url}/{id_obj}', json=data)

    assert res.status_code == 200
    assert res.json()['name'] == data['name']

    delete_object(id_obj)


def patch_object_test():
    id_obj = post_new_object()

    data = {"name": "Test Object 335"}

    res = requests.patch(f'{url}/{id_obj}', json=data)

    assert res.status_code == 200
    assert res.json()['name'] == data['name']

    delete_object(id_obj)


def delete_object_test():
    id_obj = post_new_object()

    res = requests.delete(f'{url}/{id_obj}')

    assert res.status_code == 200


post_object_test()
put_object_test()
patch_object_test()
delete_object_test()
