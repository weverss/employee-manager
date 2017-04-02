from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
