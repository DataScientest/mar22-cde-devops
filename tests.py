import requests

API_URL = "http://127.0.0.1:8000"


def test_get_hello():
    response = requests.get(
        url=f"{API_URL}/hello"
    )

    assert response.status_code == 200, response.content

    data = response.json()

    assert "message" in data
    assert data["message"] == "hello"


# GET /health
# -> {"status": 1}

def test_get_health():
    response = requests.get(
        url=f"{API_URL}/health"
    )

    assert response.status_code == 200, response.content

    data = response.json()

    assert "status" in data
    assert data["status"] == 1


# GET /
# -> message qui renvoie vers la doc

def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200, response.content

    data = response.json()

    assert "message" in data


def test_put_bye():
    response = requests.put(
        url=f"{API_URL}/bye"
    )

    assert response.status_code == 200
    data = response.json()

    assert "bye" in data
    assert data["bye"] == "bye"
