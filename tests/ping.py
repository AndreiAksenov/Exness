import requests


def test_ping():
    url = "http://localhost:5000/ping/"
    ping_resp = requests.get(url)
    assert ping_resp.status_code == 200, 'retrieve token info'
