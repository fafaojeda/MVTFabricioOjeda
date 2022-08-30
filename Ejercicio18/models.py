from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)

    email = models.EmailField()

