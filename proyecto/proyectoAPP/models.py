from django.db import models

# Create your models here.
class registro(models.Model):
    nombre =models.CharField(max_length=30)
    apellido =models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True, blank=True)