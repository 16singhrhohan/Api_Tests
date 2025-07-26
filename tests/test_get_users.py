import requests

def test_get_users_list():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    assert response.status_code == 200

    # Validate it's a list and has users
    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0
    assert "id" in users[0]
    assert "name" in users[0]
