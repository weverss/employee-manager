from rest_framework import serializers
from .models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')

    def create(self, validated_data):
        request = self.context.get("request")
        department_name = request.data.get('department')
        department, created = Department.objects.get_or_create(name=department_name)
        return Employee.objects.create(department=department, **validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        department_name = request.data.get('department')
        instance.department, created = Department.objects.get_or_create(name=department_name)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance