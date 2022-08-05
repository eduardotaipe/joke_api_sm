from starlette.status import HTTP_200_OK

from app.test.conftest import client


PREFIX_MATH_API = "/api/v1/math/"

PATH_LCM = PREFIX_MATH_API + "lcm"
NUMBERS_QUERY_STRING = "?numbers=15,2,30,4"
RESULT_LCM = {"result": 60}

PATH_PLUS_ONE = PREFIX_MATH_API + "plus_one"
NUMBER_QUERY_STRING = "?number=12"
RESULT_PLUS_ONE = {"result": 13}


def test_get_lcm_from_numbers_list():
    response = client.get(f"{PATH_LCM}{NUMBERS_QUERY_STRING}")

    assert response.status_code == HTTP_200_OK
    assert response.json() == RESULT_LCM


def test_get_number_plus_one():
    response = client.get(f"{PATH_PLUS_ONE}{NUMBER_QUERY_STRING}")

    assert response.status_code == HTTP_200_OK
    assert response.json() == RESULT_PLUS_ONE
