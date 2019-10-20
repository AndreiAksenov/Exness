import requests
import json


def user_authorize(login: str, password: str):
    url = 'http://localhost:5000/authorize/'
    auth_data = {
        'username': login,
        'password': password
    }
    auth_response = requests.post(url, data=auth_data)
    return auth_response


def get_token(response):
    js = json.loads(response.content)
    token = js['token']
    return token
