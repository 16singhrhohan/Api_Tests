import requests
import certifi

def test_create_user():
    url = "https://jsonplaceholder.typicode.com/posts"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "name": "Your Name",
        "job": "Your Position"
    }
    response = requests.post(url, json=payload, headers = headers, verify = certifi.where())

    assert response.status_code == 201
    response_json = response.json()
    assert response_json["name"] == "Your Name"
    assert response_json["job"] == "Your Position"
