from starlette.status import HTTP_200_OK
from starlette.status import HTTP_201_CREATED
from starlette.status import HTTP_204_NO_CONTENT

from app.test.utils import get_random_joke
from app.test.conftest import client


PREFIX_JOKE_API = "/api/v1/joke/"

DATA_CREATE = {
    "text": "¿Qué es un terapeuta? – 1024 Gigapeutas.",
}

DATA_UPDATE = {
    "text": "¿Qué le dice un .GIF a un .JPEG? -Anímate viejo.",
}

PATH_API_CHUCK = PREFIX_JOKE_API + "chuck"
API_CHUCK = "https://api.chucknorris.io/jokes/random"

PATH_API_DAD = PREFIX_JOKE_API + "dad"
API_DAD = "https://icanhazdadjoke.com/"

NAME_API_VALUE = "api"

RESPONSE_NO_CONTENT = ""


def test_create_joke():
    response = client.post(PREFIX_JOKE_API, json=DATA_CREATE)

    assert response.status_code == HTTP_201_CREATED
    assert response.json() == DATA_CREATE


def test_update_joke():
    joke_id = get_random_joke()

    response = client.put(f"{PREFIX_JOKE_API}{joke_id}", json=DATA_UPDATE)

    assert response.status_code == HTTP_200_OK
    assert response.json() == DATA_UPDATE


def test_get_random_joke():
    response = client.get(PREFIX_JOKE_API)

    assert response.status_code == HTTP_200_OK


def test_get_joke_from_external_api_chuck():
    response = client.get(f"{PATH_API_CHUCK}")

    assert response.status_code == HTTP_200_OK
    assert response.json()[NAME_API_VALUE] == API_CHUCK


def test_get_joke_from_external_api_dad():
    response = client.get(f"{PATH_API_DAD}")

    assert response.status_code == HTTP_200_OK
    assert response.json()[NAME_API_VALUE] == API_DAD


def test_delete_joke():
    joke_id = get_random_joke()
    response = client.delete(f"{PREFIX_JOKE_API}{joke_id}")

    assert response.status_code == HTTP_204_NO_CONTENT
    assert response.text == RESPONSE_NO_CONTENT
