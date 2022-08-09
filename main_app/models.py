from django.db import models
from django.urls import reverse

# Create your models here.
class Gundam(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'gundam_id': self.id})