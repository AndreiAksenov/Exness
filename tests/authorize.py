from fixtures.utils import *


def test_correct_username_password():
    response = user_authorize('supertest', 'superpassword')
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content


def test_receive_new_token():
    response = user_authorize('supertest', 'superpassword')
    token = get_token(response)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content

    response = user_authorize('supertest', 'superpassword')
    new_token = get_token(response)
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert token != new_token, 'these tokens are not different, body: %s' % response.content


def test_wrong_password():
    response = user_authorize('supertest', 'wrongpassword')
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_empty_password():
    response = user_authorize('supertest', '')
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_empty_username_password():
    response = user_authorize('', '')
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_without_parameters_username_password():
    response = requests.post('http://localhost:5000/authorize/')
    assert response.status_code == 403, 'unexpected status code, body: %s' % response.content


def test_token_response_time():
    response = user_authorize('supertest', 'superpassword')
    assert response.status_code == 200, 'unexpected status code, body: %s' % response.content
    assert response.elapsed.total_seconds() < 1
