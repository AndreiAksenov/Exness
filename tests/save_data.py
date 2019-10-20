from fixtures.utils import *
import time
import requests


def test_user_with_valid_token():
    token = authorize_token('supertest', 'superpassword')
    payload = random_payload()
    response = user_save_data(token, payload)
    js = json.loads(response.content)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert js['status'] == 'OK', 'unexpected status, body: %s' % js['error']


def test_user_data_save_into_db():
    token = authorize_token('supertest', 'superpassword')
    payload = random_payload()
    response = user_save_data(token, payload)
    js = json.loads(response.content)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert js['status'] == 'OK', 'unexpected status, body: %s' % js['error']

    id_record = js['id']
    payload_md5 = encode_payload_for_db(payload)
    payload_md5_from_db = get_payload_md5_from_db(id_record)
    assert payload_md5 == payload_md5_from_db


def test_save_data_several_times_with_valid_token():
    token = authorize_token('supertest', 'superpassword')
    response = user_save_data(token, '65451')
    js = json.loads(response.content)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert js['status'] == 'OK', 'unexpected status, body: %s' % js['error']

    response = user_save_data(token, '98456')
    js = json.loads(response.content)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert js['status'] == 'OK', 'unexpected status, body: %s' % js['error']

    response = user_save_data(token, '32156')
    js = json.loads(response.content)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert js['status'] == 'OK', 'unexpected status, body: %s' % js['error']


def test_user_without_token():
    payload = random_payload()
    response = user_save_data(payload)
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_user_without_valid_token():
    payload = random_payload()
    response = user_save_data('', payload)
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_user_without_auth_header():
    payload = random_payload()
    data = {
        'payload': payload
    }
    response = requests.post('http://localhost:5000/api/save_data/', data=data)
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_user_without_payload():
    token = authorize_token('supertest', 'superpassword')
    response = user_save_data(token, '')
    assert response.status_code == 400, 'unexpected status code, body: %s' % response.content


def test_user_with_expired_token():
    token = authorize_token('supertest', 'superpassword')
    payload = random_payload()
    time.sleep(60)
    response = user_save_data(token, payload)
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_save_data_response_time():
    token = authorize_token('supertest', 'superpassword')
    payload = random_payload()
    response = user_save_data(token, payload)
    js = json.loads(response.content)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert js['status'] == 'OK', 'unexpected status, body: %s' % js['error']
    assert response.elapsed.total_seconds() < 1

