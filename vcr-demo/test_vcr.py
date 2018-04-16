import requests
import vcr


@vcr.use_cassette('cassettes/test_vhs')
def test_vhs():
    response = requests.get('https://www.example.com')
    assert response.status_code == 200
