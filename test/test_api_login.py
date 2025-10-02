
import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    print("Response:", response.json())  # Optional debug
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
