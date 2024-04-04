# Este archivo contiene los datos para las solicitudes POST utilizados en las pruebas.

def get_kit_body(name):
    return {"name": name} if name is not None else {}

# Ejercicio #1: Nombre válido con 1 carácter
# Prueba si la API acepta un nombre de kit con un solo carácter.
kit_body_1_char = get_kit_body("a")

# Ejercicio #2: Nombre válido con 511 caracteres
# Prueba si la API rechaza un nombre de kit con 511 caracteres.

kit_body_511_chars = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

# Ejercicio #3: Nombre vacío
# Prueba si la API rechaza un nombre de kit vacío.
kit_body_empty = get_kit_body("")

# Ejercicio #4: Nombre con más de 512 caracteres
# Prueba si la API rechaza un nombre de kit con más de 512 caracteres.
kit_body_512_chars = get_kit_body("BAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Ejercicio #5: Nombre con caracteres especiales
# Prueba si la API acepta un nombre de kit con caracteres especiales.
kit_body_special_chars = get_kit_body("№%@\"")

# Ejercicio #6: Nombre con espacios
# Prueba si la API acepta un nombre de kit con espacios.
kit_body_spaces = get_kit_body(" A Aaa ")

# Ejercicio #7: Nombre numérico como cadena
# Prueba si la API acepta un nombre de kit numérico como cadena.
kit_body_numeric_string = get_kit_body("123")

# Ejercicio #8: Sin parámetro 'name'
# Prueba si la API rechaza una solicitud sin el parámetro 'name'.
kit_body_no_param = get_kit_body(None)

# Ejercicio #9: Tipo de parámetro diferente (número en lugar de cadena)
# Prueba si la API rechaza un nombre de kit que es un número en lugar de una cadena.
kit_body_numeric_type = {"name": 123}

