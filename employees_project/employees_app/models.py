from django.db import models


# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.CharField(max_length=30)
