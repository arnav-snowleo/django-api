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

# SERIALIZERS
> python representation of data <-> json
> serializers used to define how we want this data conversion to be like

# Viewset.
> by defining EmployeeViewset. it creates classes like list(), retrieve() , create() , update() , destroy()
> for web methods like get put post

> To run -> ```localhost:8000/api/employee/```
