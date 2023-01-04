from django.db import models


class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200)
    priority = models.IntegerField()

