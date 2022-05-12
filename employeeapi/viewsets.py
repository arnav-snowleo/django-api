from rest_framework import viewsets

from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewset):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer

# by defining EmployeeViewset. it creates classes like list(), retrieve() , create() , update() , destroy()
# for web methods like get put post