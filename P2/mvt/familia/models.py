from django.db import models

class familiares(models.Model):
    name = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha = models.DateField()