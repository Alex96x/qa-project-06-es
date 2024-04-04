# Proyecto 6 WILLIAM VASQUEZ COHORT 08 

# Pruebas Automatizadas con Python

Este proyecto consiste en una serie de pruebas automatizadas para una API que permite crear un "kit" para un usuario específico o para una tarjeta específica.

## Archivos del Proyecto

El proyecto consta de los siguientes archivos:

- `configuration.py`: Contiene las constantes utilizadas en las solicitudes a la API, como la URL del servicio, las rutas de la API y los encabezados de las solicitudes.
- `data.py`: Contiene los cuerpos de las solicitudes POST utilizados en las pruebas.
- `sender_stand_request.py`: Contiene las funciones que hacen las solicitudes POST a la API para crear un usuario y un kit.
- `create_kit_name_kit_test.py`: Contiene las funciones de prueba para cada uno de los ejercicios.
- `.gitignore`: Especifica los archivos y directorios que Git debe ignorar.
- `README.md`: Este archivo, que proporciona una descripción del proyecto y las instrucciones para ejecutar las pruebas.

## Cómo Ejecutar las Pruebas

Para ejecutar las pruebas, sigue estos pasos:

1. Asegúrate de tener instalado Python y la biblioteca `requests`.
2. Clona este repositorio en tu máquina local.
3. Abre una terminal y navega hasta el directorio del proyecto.
4. Ejecuta el archivo `create_kit_name_kit_test.py` con el comando `python create_kit_name_kit_test.py`.

## Resultados de las Pruebas

Algunas pruebas devolverán FAILED como resultado, esto es un comportamiento esperado dentro de la lista de comprobaciones.
