from django.db import models

# Create your models here.
class registro(models.Model):
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    fecha_nacimiento = models.DateField()
    descripcion = models.TextField()
    imagen = models.ImagenField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
