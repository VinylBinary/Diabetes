from django.db import models

# Create your models here.

class data(models.Model):
    Name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length = 10)
    smoke = models.BooleanField()
    audio = models.FileField(upload_to = 'audio/')
