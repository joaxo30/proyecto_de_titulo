from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('cajero', 'Cajero'),
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROLES)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.usuario})"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.categoria}"