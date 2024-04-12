# Proyecto 6 WILLIAM VASQUEZ COHORT 08
## Pruebas Automatizadas con Python

Este proyecto consiste en una serie de pruebas automatizadas para una API que permite crear un "kit" para un usuario específico o para una tarjeta específica. Las pruebas se han mejorado para evitar la repetición de código y para manejar mejor los errores de red y los códigos de estado HTTP inesperados.

## Archivos del Proyecto

El proyecto consta de los siguientes archivos:

- `configuration.py`: Contiene las constantes utilizadas en las solicitudes a la API, como la URL del servicio, las rutas de la API y los encabezados de las solicitudes.
- `data.py`: Contiene los datos de prueba utilizados en las pruebas. Los datos de prueba se organizan en una lista de diccionarios para facilitar su uso con la función `parametrize` de pytest.
- `sender_stand_request.py`: Contiene las funciones que hacen las solicitudes POST a la API para crear un usuario y un kit. Estas funciones ahora incluyen manejo de errores para detectar y manejar los errores de red y los códigos de estado HTTP inesperados.
- `create_kit_name_kit_test.py`: Contiene las funciones de prueba para cada uno de los ejercicios. Las pruebas se han refactorizado para evitar la repetición de código y para utilizar la función `parametrize` de pytest.
- `.gitignore`: Especifica los archivos y directorios que Git debe ignorar.
- `README.md`: Este archivo, que proporciona una descripción del proyecto y las instrucciones para ejecutar las pruebas.

## Cómo Ejecutar las Pruebas

Para ejecutar las pruebas, sigue estos pasos:

1. Asegúrate de tener instalado Python y la biblioteca requests.
2. Clona este repositorio en tu máquina local.
3. Abre una terminal y navega hasta el directorio del proyecto.
4. Ejecuta el archivo `create_kit_name_kit_test.py` con el comando `python create_kit_name_kit_test.py`.

## Resultados de las Pruebas

Algunas pruebas devolverán FAILED como resultado, esto es un comportamiento esperado dentro de la lista de comprobaciones. Las pruebas que se esperan que fallen están diseñadas para probar los límites de la API y asegurarse de que la API maneja correctamente las solicitudes inválidas.
