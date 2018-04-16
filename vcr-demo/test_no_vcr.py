import requests


def test_no_vhs():
    response = requests.get('https://www.example.com')
    assert response.status_code == 200
