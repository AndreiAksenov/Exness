import requests
import json
import random
import sqlite3
import hashlib


def random_payload():
    return random.randint(10000, 99999)


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


def authorize_token(login, password):
    url = 'http://localhost:5000/authorize/'
    auth_data = {
        'username': login,
        'password': password
    }
    response = requests.post(url, data=auth_data)
    js = json.loads(response.content)
    token = js['token']
    return token


def user_save_data(token=None, payload=None):
    url = 'http://localhost:5000/api/save_data/'
    if token is None:
        header = {
            'Authorization': ''
        }
    else:
        header = {
            'Authorization': 'Bearer %s' % token
        }
    data = {
        'payload': payload
    }
    auth_response = requests.post(url, headers=header, data=data)
    return auth_response


def encode_payload_for_db(payload):
    payload_md5 = hashlib.md5(str(payload).encode('utf-8')).hexdigest()
    return payload_md5


def get_payload_md5_from_db(id_record):
    conn = sqlite3.connect("D:/Projects/Exness/venv/bin\main.db")
    cursor = conn.cursor()
    sql = "SELECT payload_md5 FROM uploads WHERE id = %s " % id_record
    cursor.execute(sql)
    payload_md5 = cursor.fetchall()[0]
    return payload_md5[0]


def check_record_in_db(id_record):
    conn = sqlite3.connect("D:/Projects/Exness/venv/bin\main.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM uploads WHERE id = %s " % id_record
    cursor.execute(sql)
    payload_md5 = cursor.fetchall()[0]
    return payload_md5[0]
