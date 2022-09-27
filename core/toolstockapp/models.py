from django.db import models

# Create your models here.
class Grupo(models.Model):
    nombre = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)

class Unidad(models.Model):
    medida = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.medida

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    #falta id de la ciudad llave foranea
    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    #falta id Unidad, id Proveedor, id Grupo
    def __str__(self) -> str:
        return self.nombre