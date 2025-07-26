import requests

def test_update_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {
        "id": 1,
        "title": "Your Name",
        "body": "Your New Position",
        "userId": 1
    }
    response = requests.put(url, json=payload)

    assert response.status_code == 200  # JSONPlaceholder simulates success
    response_json = response.json()

    assert response_json["title"] == "Your Name"
    assert response_json["body"] == "Your New Position"
    assert response_json["userId"] == 1
