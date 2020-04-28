<div align="center">
  <h1>Guía para proyectos en Django</h1>
</div>

<div align="center">
  <img src="./readme_img/django.png"
    width="60%"
   alt="hello-world-capture">
</div>

## Configuración de entorno de trabajo
Primero debemos tener instalado Python. Luego de la instalacion abrimos la terminal y nos posicionamos en la ruta que deseamos establecer nuestro proyecto.

## Creacion de entorno virtual con Python
Vamos a crear un entorno virtual para nuestro proyecto, el cual contendra todas las dependencias. Es muy importante que este entorno este fuera de nuestro proyecto. Para crearlo ejecutamos:
```
python -m venv .env
```
Nota: .env sera el nombre de nuestro entorno.

## Comandos del entorno

Para **activar** nuestro entorno ejecutamos
```
source .env/bin/activate
```
Y para **desactivarlo**
```
deactivate
```
Si queremos **listar las librerias instaladas** usamos
```
pip freeze
```
## Instalación de Django
Para **instalar** la ultima version de Django ejecutamos
```
pip install django -U
```
## Django Admin
Es una interfaz instalada junto con Django que contiene subcomandos que utiles. Para listar los subcomandos utilizamos
```
django-admin
```
## Creacion de proyecto
Para **crear** un proyecto ejecutamos
```
django-admin startproject name
```
## Exploracion de los archivos
Lo primero que veremos es un folder con el nombre de nuestro proyecto, el cual contiene los archivos:

- **\_\_init_\_.py:** la unica finalidad de este archivo es declarar nuestra carpeta como un modulo de python.
- **settings.py:** es el mas importante, define todas las configuraciones de nuestro proyecto.
- **urls.py:** es el archivo de punto de entrada para todas las peticiones a nuestro proyecto.
- **wsgi.py:** es usado para el deployment a produccion y es la interfaz WSGI cuando el servidor corre en producción.
- **manage.py:** es un archivo que no tocamos, pero interactuamos con el durante todo el desarrollo.
## Archivo settings.py
Dentro del archivo setting podemos encontrar variables relevantes para nuestro proyecto, las cuales son:
- **BASE_DIR:** Declara el lugar donde esta corriendo el proyecto. Se considera la linea mas importante.
- **SECRET_KEY:** Es utilizado para el hashing de las contraseñas y las sesiones que se almacenan en las bases de datos.
- **DEBUG:** Determina si nuestro proyecto se encuentra en desarrollo.
- **ALLOWED_HOSTS:** Lista los host que estan permitidos para interactuar con nuestro proyecto.
- **INSTALLED_APPS:** Lista las aplicaciónes instaladas y ligadas a nuestro proyecto.
- **MIDDLEWARE:** Lista los middleware instalados y ligados a nuestro proyecto.
- **ROOT_URLCONF:** Define el archivo principal de urls.
- **TEMPLATES:** Los templates de nuestras aplicaciónes.
- **WSGI_APPLICATION:** Archivo de entrada de nuestro WSGI.
- **DATABASES:** Almacena las configuraciones de las bases de datos.
- **AUTH_PASSWORD_VALIDATORS:** Los validadores de contraseñas.
- **LANGUAGE_CODE:** El idioma en el que se interactua con nuestra aplicación.
- **TIME_ZONE:** Zona horaria en el cual corre nuestra aplicación.
- **STATIC_URL:** En lugar de resolver la url establecidas en el archivo de urls, va a buscar resolver el archivo estático con la url estalecida en esta variable.
## Archivo manage.py
Este archivo contiene un gran listado de subcomandos los cuales podemos listar con:
```
python manage.py
```
## Levantar servicio
Para levantar el servicio ejecutamos:
```
python manage.py runserver
```
## Crear la primera vista
Para este ejercicio lo haremos simple. En el archivo **urls.py** importamos **django.http.HttpResponse** y definimos una **funcion** que devuelva una respuesta (en este caso hello_world), y establemos en que path estara esta despuesta:
```
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello, world!')

urlpatterns = [
    path('hello-world', hello_world)
]
```
Corremos nuestro servidor con
```
python manage.py runserver
```
Luego accedemos al **localhost:8000/hello-world** donde podremos acceder a nuestra vista:

<div align="center">
  <img src="./readme_img/hello_world.png"
    width="100%"
   alt="hello-world-capture">
</div>