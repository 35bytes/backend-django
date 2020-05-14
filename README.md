<div align="center">
  <h1>Guía para proyectos en Django</h1>
</div>

<div align="center">
  <img src="./readme_img/django_2.png"
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

```py
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello, world!')

urlpatterns = [
    path('hello-world/', hello_world)
]
```

Corremos nuestro servidor con

```
python manage.py runserver
```

Luego accedemos al [**http://localhost:8000/hello-world**](http://localhost:8000/hello-world) donde podremos acceder a nuestra vista:

<div align="center">
  <img src="./readme_img/hello_world.png"
    width="100%"
   alt="hello-world-capture">
</div>


## Como Django procesa un request
1. Primero va a buscar en el archivo **settings.py** en la variable **ROOT_URLCONF**
2. Luego Django desde el archivo **urls.py** carga los modulos de Python definidos en la variable **urlpatterns**
3. Dentro de **urlpatterns** se busca el patron coincidente a la peticion
4. Una vez encontrado la URL que coincide, Django importa y llama la vista en una funcion simple en Python. Se le pasa como argumento:
    - Una instancia del HttpRequest
    - Si la URL pasa mas argumentos entonces los entregara
    - Si definimos argumentos adicionales tambien lo enviara
5. Si ninguna URL coincide, Django enviara una excepción

## Separando las vistas
Es buena practica tener las vistas separadas del archivo url.py, por lo que crearemos un archivo **views.py** dentro de nuestra aplicación que contendra las vistas:

<div align="center">
  <img src="./readme_img/views.png"
    width="40%"
   alt="hello-world-capture">
</div>

Dentro de nuestro archivo **views.py** importamos **HttpResponse** y traemos nuestra funcion **hello_world()** creado en urls.py

```py
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello, world!')
```

Ahora debemos importar nuestra funcion al archivo **urls.py**.
No olvidemos **borrar** la importacion de HttpResponse y la funcion hello_world() en el archivo.

```py
from django.contrib import admin
from django.urls import path
from photogram import views

urlpatterns = [
    path('hello-world/', views.hello_world)
]
```

Si revisamos la url [**http://localhost:8000/hello-world**](http://localhost:8000/hello-world) nuestro proyecto seguira funcionando.

## El objeto Request
A traves del objeto request podemos acceder a varios atributos  los cuales se encuentran detallados en la [documentación](https://docs.djangoproject.com/en/3.0/ref/request-response/) de Django. Algunos atributos utiles son:

- **request.method:** nos muestra el metodo HTTP ("GET", "POST", etc.) usado por el request en formato de string en UPPERCASE. Un ejemplo de uso seria:

  ```py
  if request.method == 'GET':
      do_something()
  elif request.method == 'POST':
      do_something_else()
  ```

- **request.GET:** Un diccionario que contiene todos los parametros entregados por HTTP GET. Por ejemplo:

  Pasamos una lista de numeros en la variable numbers **(?numbers)**

  ```http
  http://localhost:8000/numbers/?numbers=10,2,6,7
  ```

  Para acceder a la lista usamos 

  ```py
  request.GET['numbers']
  ```

  *Nota: En el siguiente ejemplo se creo la vista numbers*
  
  Un ejemplo practico seria:

  ```py
  def numbers(request):
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))
  ```

  De esta forma podemos ver los valores de number a traves de nuetra vista.

  <div align="center">
    <img src="./readme_img/numbers.png"
      width="100%"
    alt="numbers">
  </div>

## Pasando argumentos por URL
Podemos pasar argumentos a traves de la URL, para esto primero creamos la funcion que hara uso de estos parametros y devolvera la vista en el archivo **views.py**
```py
from django.http import HttpResponse

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}! Welcome to Photogram'.format(name)
    
    return HttpResponse(message)
```

Luego definimos el path para esta vista en el archivo **urls.py**. Para definir los parametros que pasaran por la url los encerramos con "<>" definiendo el tipo de dato y el nombre del parametro.

```py
from django.contrib import admin
from django.urls import path
from photogram import views

urlpatterns = [
    path('hi/<str:name>/<int:age>/', views.say_hi)
]
```

En el resultado final si ingresamos **age = 26** y **name = Karl** obtenemos el resultado definido en nuestra funcion **say_hi()**:

<div align="center">
    <img src="./readme_img/url_params_1.png"
      width="70%"
    alt="numbers">
</div>

Pero si cambiamos **age = 10** obtenemos:

<div align="center">
    <img src="./readme_img/url_params_2.png"
      width="70%"
    alt="numbers">
</div>

## Crear una app
Con Django podemos crear una app de forma rapida y sencilla ejecutando el comando

```
python manage.py startapp name
```

En este ejemplo creamos un app llamada **posts**, el cual genero una carpeta con todos los archivos basicos necesarios

<div align="center">
    <img src="./readme_img/app_posts.png"
      width="40%"
    alt="numbers">
</div>

Para desplegar una vista de esta aplicacion vamos al archivo *./posts/views.py* donde crearemos una vista a traves de la funcion **list_posts()**

```py
from django.shortcuts import render
from django.http import HttpResponse

def list_posts(request):
    posts = [1, 2, 3, 4]
    return HttpResponse(str(posts))
```

Luego vamos al archivo settings de nuestro proyecto, en este caso *./photogram/settings.py* donde incorporaremos en la variable **INSTALLED_APPS** nuestra nueva app

```py
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'posts',
]
```

Ahora nos toca asignar un path para nuestra vista **list_posts()**. Para eso vamos al archivo **urls.py** de nuestro proyecto, en este caso *./photogram/urls.py* e importamos nuestra nueva app, y le asignamos un path a nuestra vista.

Para que no existan conflictos al llamar views vamos asignar un **alias** para las views de cada aplicacion.

```py
from django.contrib import admin
from django.urls import path
from photogram import views as local_views

# Importamos las vistas de nuestra aplicacion posts
from posts import views as posts_views

urlpatterns = [
    
    path('hello-world/', local_views.hello_world),
    path('numbers/', local_views.numbers),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),

    # Asignamos el path para nuestra vista list_posts
    path('posts/', posts_views.list_posts),

]
```

Ahora vamos a [**http://localhost:8000/posts/**](http://localhost:8000/posts/) para ver nuestro resultado

<div align="center">
    <img src="./readme_img/posts.png"
      width="80%"
    alt="numbers">
</div>

## Template system

El template system es una manera de mostrar los datos usando HTML, incluye lógica de programacion lo cual nos facilita un poco el crear nuestros templates.

Para crear nuestros templates lo que haremos es dentro de nuestra aplicacion **crear una carpeta templates** y un **archivo html** con el nombre de nuestro template, en este caso _feed.html_

<div align="center">
    <img src="./readme_img/template_feed.png"
      width="40%"
    alt="numbers">
</div>

Dentro de nuestro archivo **feed.html** solo escribiremos:

```html
Hola, mundo!
```

Y dentro de **views.py** de nuestra aplicación ya no es necesario el HttpResponse, por que borramos su importación. A través de la función que devolvemos nuestra vista devolveremos nuestro nuevo template con el metodo **render**, que le pasaremos la request y la vista:

```py
from django.shortcuts import render

def list_posts(request):
    return render(request, 'feed.html')
```

Si revisamos el path [**http://localhost:8000/posts/**](http://localhost:8000/posts/) tendremos nuestro "Hola, mundo!"

<div align="center">
    <img src="./readme_img/post_hola_mundo.png"
      width="80%"
    alt="numbers">
</div>

¿Como logro funcionar si dentro de render jamas definimos la ruta donde buscar nuestro template? (en nuetro caso solo _feed.html_). Si revisamos en el archivo **settings.py** de nuestro proyecto, en la definicion de **TEMPLATES** veremos

```py

...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...

```

En **APP_DIRS** lo tenemos definido como **True**, esto significa que las aplicaciones buscaran los templates dentro de sus directorios, de esta forma funciona sin tener que nombrar la dirección de nuestro template.

## Pasando datos a nuestro template

Primero crearemos un diccionario de datos dentro de nuestra vista (solo a modo de ejemplo) y enviaremos al template estos datos a traves del render. En nuestro caso este diccionario sera posts

```py
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html', {'posts': posts})
```

Si logran observar enviamos los datos a traves de **{'posts': posts}**, el cual el **primer parametro sera el nombre de la variable** al momento de enviar al template, y el **segundo es el valor asignado**.

En nuestro template _feed.html_ ahora imprimiremos nuestro diccionario escribiendo el **nombre de la variable**.

```html
{{ posts }}
```

Si revisamos [**http://localhost:8000/posts/**](http://localhost:8000/posts/) veremos nuestro diccionario.

<div align="center">
    <img src="./readme_img/posts_diccionario.png"
      width="80%"
    alt="numbers">
</div>

Ahora juguemos un poco con la **lógica de programación** y **html**. Vamos a imprimir solo los títulos. Para eso en nuestro **template** _feed.html_ escribiremos:

```html
{% for post in posts %}
  <p>{{ post.title }}</p>
{% endfor %}
```

Y el resultado en [**http://localhost:8000/posts/**](http://localhost:8000/posts/)

<div align="center">
    <img src="./readme_img/posts_diccionario_titulos.png"
      width="80%"
    alt="numbers">
</div>

Para ver toda la **lógica de programación** que podemos crear en el template system te recomiendo ir a la [documentación de Django.](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

Ahora despleguemos los datos de nuestro diccionario y estilemos con **Bootstrap** nuestro template _feed.html_.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Platzigram</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
</head>
<body>
  <br><br>
  <div class="container">
    <div class="row">
      {% for post in posts %}
      <div class="col-lg-4 offset-lg-4">
        <div class="media">
          <img class="mr-3 rounded-circle" src="{{ post.user.picture }}" alt="{{ post.user.name }}">
          <div class="media-body">
            <h5 class="mt-0">{{ post.user.name }}</h5>
            {{ post.timestamp }}
          </div>
        </div>
        <img class="img-fluid mt-3 border rounded" src="{{ post.photo }}" alt="{{ post.title }}">
        <h6 class="ml-1 mt-1">{{ post.title }}</h6>
      </div>
      {% endfor %}
    </div>
    </div>
</body>
</html>

```

Y en [**http://localhost:8000/posts/**](http://localhost:8000/posts/) veremos
:
<div align="center">
    <img src="./readme_img/estilado.gif"
      width="40%"
    alt="numbers">
</div>

## Creacion de Super Usuario

Para crear un **super usuario** en Django es bastante facil. En la consola escribimos

```
python3 manage.py createsuperuser
```

Nos preguntara un **username, email (opcional), y contrañesa**, con esto ya tendriamos nuestro super usuario.

## Dashboard de Administración

Django cuenta con un dashboard de administración. Para acceder a el debemos darle un path dentro del archivo **urls.py** de nuestro proyecto. Para esto importamos **django.contrib.admin** y le asignamos la dirección que deseamos

```py
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
```

En este caso le dimos el path **/admin/** para acceder a el. Entonces vamos a la dirección [**http://localhost:8000/admin/**](http://localhost:8000/admin/) para ingresar.

<div align="center">
    <img src="./readme_img/dashboard_login.png"
      width="60%"
    alt="numbers">
</div>

Para ingresar utilizaremos el **super usuario** que creamos en la [**sección de creación de super usuario.**](#creacion-de-super-usuario)