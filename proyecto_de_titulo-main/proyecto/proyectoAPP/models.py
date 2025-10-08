from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    password = models.CharField(max_length=128) 
    fecha_nacimiento = models.DateField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"