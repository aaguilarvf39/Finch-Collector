from django.db import models

# Create your models here.
class Gundam(models.Model):
    name = models.CharField(max_length=100)
    skill = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    year = models.IntegerField()