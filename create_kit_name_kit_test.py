from sender_stand_request import create_user, create_kit
from data import get_kit_body

def test_create_kit_with_one_character_name():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body = get_kit_body("a")
    kit_response = create_kit(auth_token, kit_body)

    # Verificar creación de kit
    assert kit_response.status_code == 201, "Error al crear kit"
    assert kit_response.json().get('name') == kit_body['name'], "El nombre del kit no coincide"

def test_create_kit_with_511_character_name():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit

    kit_body_511_chars = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_response = create_kit(auth_token, kit_body_511_chars)

    # Verificar que la creación de kit falla
    assert kit_response.status_code == 201, "Error: se pudo crear un kit con un nombre de 511 caracteres"

def test_create_kit_with_empty_name():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body = get_kit_body("")
    kit_response = create_kit(auth_token, kit_body)

    # Verificar que la creación de kit falla
    assert kit_response.status_code == 400, "Error: se pudo crear un kit con un nombre vacío"

def test_create_kit_with_512_character_name():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body_512_chars = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_response = create_kit(auth_token, kit_body_512_chars)

    # Verificar que la creación de kit falla
    assert kit_response.status_code == 400, "Error: se pudo crear un kit con un nombre de 512 caracteres"

def test_create_kit_with_special_characters():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body_special_chars = get_kit_body("№%@\"")
    kit_response = create_kit(auth_token, kit_body_special_chars)

    # Verificar creación de kit
    assert kit_response.status_code == 201, "Error al crear kit"
    assert kit_response.json().get('name') == kit_body_special_chars['name'], "El nombre del kit no coincide"

def test_create_kit_with_spaces():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body_spaces = get_kit_body(" A Aaa ")
    kit_response = create_kit(auth_token, kit_body_spaces)

    # Verificar creación de kit
    assert kit_response.status_code == 201, "Error al crear kit"
    assert kit_response.json().get('name') == kit_body_spaces['name'], "El nombre del kit no coincide"

def test_create_kit_with_numeric_string():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body_numeric_string = get_kit_body("123")
    kit_response = create_kit(auth_token, kit_body_numeric_string)

    # Verificar creación de kit
    assert kit_response.status_code == 201, "Error al crear kit"
    assert kit_response.json().get('name') == kit_body_numeric_string['name'], "El nombre del kit no coincide"

def test_create_kit_without_name_param():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body_no_param = get_kit_body(None)
    kit_response = create_kit(auth_token, kit_body_no_param)

    # Verificar que la creación de kit falla
    assert kit_response.status_code == 400, "Error: se pudo crear un kit sin el parámetro 'name'"

def test_create_kit_with_numeric_type():
    # Crear usuario
    user_data = {
        "firstName": "Max",
        "phone": "+10005553535",
        "address": "8042 Lancaster Ave.Hamburg, NY"
    }
    user_response = create_user(user_data)

    # Verificar creación de usuario
    assert user_response.status_code == 201, "Error al crear usuario"
    auth_token = user_response.json().get('authToken')

    # Crear kit
    kit_body_numeric_type = {"name": 123}
    kit_response = create_kit(auth_token, kit_body_numeric_type)

    # Verificar que la creación de kit falla
    assert kit_response.status_code == 400, "Error: se pudo crear un kit con un nombre de tipo numérico"

# Ejecutar pruebas
test_create_kit_with_one_character_name()
test_create_kit_with_511_character_name()
test_create_kit_with_empty_name()
test_create_kit_with_512_character_name()
test_create_kit_with_special_characters()
test_create_kit_with_spaces()
test_create_kit_with_numeric_string()
test_create_kit_without_name_param()
test_create_kit_with_numeric_type()
