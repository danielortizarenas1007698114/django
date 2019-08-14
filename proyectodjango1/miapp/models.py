from django.db import models

# Create your models here.

class Libro(models.Model):
    nombre = models.CharField(max_length=45)
    decripcion = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)

