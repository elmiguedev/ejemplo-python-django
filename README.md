# ejemplo-python-django

1- pyenv local 3.12  
2- python -m venv ./venv  
3- ./venv/Scripts/Activate  
4- pip install django  
5- django-admin   startproject server .  
6- tenemos que habilitar las rutas para la app en el archivo urls.py agregando:

```
    path('', include('src.urls'))
```
7 - tenemos que crear: 

- carpeta modelos
- carpeta controllers
- carpeta serializers
- carpeta repositories

