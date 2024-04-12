import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH, HEADERS

def create_user(user_data):
    response = requests.post(f"{URL_SERVICE}{CREATE_USER_PATH}", headers=HEADERS, json=user_data)
    response.raise_for_status()  # Lanza una excepción si la solicitud falla
    return response

def create_kit(auth_token, kit_body):
    headers = {'Authorization': f'Bearer {auth_token}', **HEADERS}
    response = requests.post(f"{URL_SERVICE}{KITS_PATH}", headers=headers, json=kit_body)
    response.raise_for_status()  # Lanza una excepción si la solicitud falla
    return response
