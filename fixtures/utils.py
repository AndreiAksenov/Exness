import requests


def user_authorize(login: str, password: str):
    url = 'http://localhost:5000/authorize/'
    auth_data = {
        'username': login,
        'password': password
    }
    auth_response = requests.post(url, data=auth_data)
    assert auth_response.status_code == 200, 'unexpected status code, body: %s' % auth_response.content
