# Ecommerce Django
Mini e-commerce (catálogo de productos) donde se puede:

## Ver la lista de productos con su foto, nombre y precio.
Agregar un producto nuevo desde un formulario en HTML con Javascript, incluyendo la foto, que queda guardada en el backend (base de datos + carpeta de archivos).

## Tecnologías usadas
Python
Django
PostgreSQL
HTML5
CSS3
JavaScript

## Requisitos
Antes de ejecutar es necesario tener instalado

Python 3.14.0
Git
PostgreSQL

## Instalación
Se instala el entorno virtual con `python -m venv proyecto_django01`:


Una vez instalado el entorno debemos activarlo:

`nombre_del_entorno/Scripts/Activate.ps1`

## Dependencias
Debemos recurrir al archivo requirements.txt donde se alojan todas las dependencias a instalar necesarias con el siguiente comando:

`pip install -r requirements.txt`

## Variables de entorno
En este proyecto son necesarias variables de entorno alojadas en el archivo .env. En este repo se encuentra el .env.example con toda la información necesaria para crear el propio .env localmente.

Cabe resaltar que los datos ingresados en este archivo de varianles de entorno deben coincidir para que la conexión con postgreSQL sea exitosa.

## Migraciones
Hasta este punto solo nos queda realizar la migración de nuestros modelos al motor de base de datos de postgreSQL(ya se debe tener la base de datos creada), los ejecutamos con los siguientes comandos:

`python manage.py makemigrations`

Y luego:

`python manage.py migrate`

Con esto quedan listas tablas de nuestra base de datos.

## Ejecutar
Por último, solo nos queda correr nuestro servidor Django con el siguiente comando:

`python manage.py runserver`

El nos dará una dirección URL para que realicemos nuestras pruebas y funcionalidad, usualmente la dirección dada es parecida a esta:

http://127.0.0.1:8000/