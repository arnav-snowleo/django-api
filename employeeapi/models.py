from django.db import models

#Null	If True, Django will store empty values as NULL in the database. Default is False.
#Blank	If True, the field is allowed to be blank. Default is False.

class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    emp_id = models.IntegerField(null=False, blank=False)
    salary = models.IntegerField(null=True, blank=True)
