import pytest
from data import test_data
from sender_stand_request import create_user, create_kit

def setup_user():
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)
    assert user_response.status_code == 201, "Error al crear usuario"
    return user_response.json().get('authToken')

@pytest.mark.parametrize("test_case", test_data)
def test_create_kit(test_case):
    auth_token = setup_user()
    kit_body = {"name": test_case["name"]}
    kit_response = create_kit(auth_token, kit_body)

    assert kit_response.status_code == test_case["expected_status"], "Error al crear kit"
    if test_case["expected_status"] == 201:
        assert kit_response.json().get('name') == kit_body['name'], "El nombre del kit no coincide"