from django.db import models
from django.urls import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    test_score = models.FloatField()

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.pk})
