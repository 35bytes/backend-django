<div align="center">
  <h1>Guía para proyectos en Django</h1>
</div>

## Configuración de entorno de trabajo
Primero debemos tener instalado Python. Luego de la instalacion abrimos la terminal y nos posicionamos en la ruta que deseamos establecer nuestro proyecto.

## Creacion de entorno virtual con Python
Vamos a crear un entorno virtual para nuestro proyecto, el cual contendra todas las dependencias. Es muy importante que este entorno este fuera de nuestro proyecto. Para crearlo ejecutamos:
```
python -m venv .env
```
Nota: .env sera el nombre de nuestro entorno

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