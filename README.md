# django-api

superuser 

username: djangooadmin1234
pw: djangoadmin1234

``` python manage.py startproject firstDjangoAPI ```
``` python manage.py startapp employeepi ```

> After db connection in settings.py , do ``` python manage.py migrate ``` this will add default tables in postgres db

> Then make model in models.py and execute to see changes in pgadmin: 
    1. python manage.py makemigrations employeeapi
    2. python manage.py migrate
