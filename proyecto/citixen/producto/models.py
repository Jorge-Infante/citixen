from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.categoria}'


class Producto(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=6, decimal_places=2)
    nombre = models.CharField(max_length=255, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Producto {self.id}:{self.categoria} - {self.nombre} - {self.precio} - {self.stock}'


class CompraProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
