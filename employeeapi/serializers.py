# python representation of data <-> json
# serializers used to define how we want this data conversion to be like


from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ('full_name' , 'salary')
