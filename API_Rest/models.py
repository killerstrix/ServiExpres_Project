from django.db import models


# Create your models here.
class Producto(models.Model):
    
    Id_Producto = models.CharField(primary_key=True, max_length=7)
    Nombre_Producto = models.CharField(max_length=30)
    stock_Producto = models.IntegerField()
    descripcion_Producto = models.CharField(max_length=100)
    Precio_Producto = models.IntegerField()
    Categoria_Producto = models.CharField(max_length=30)
    Marca_Producto = models.CharField(max_length=30)
    Proveedor_Producto = models.CharField(max_length=40)

    def __str__(self):
        return self.Nombre_Producto




class Servicio(models.Model):
    Id_Servicio = models.CharField(primary_key=True, max_length=7)
    Nombre_Servicio = models.CharField(max_length=30)
    Tipo_Servicio = models.CharField(max_length=20)
    Precio_Servicio = models.IntegerField()
    Personal_cargo = models.CharField(max_length=40)

    def __str__(self):
        return self.Nombre_Servicio


class Cuenta_Empleado(models.Model):
    Id_Empleado = models.CharField(primary_key=True, max_length=7)
    Primer_Nombre = models.CharField(max_length=20)
    Segundo_Nombre = models.CharField(max_length=20)
    Primer_Apellido = models.CharField(max_length=20)
    Segundo_Apellido = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=20)
    Edad = models.IntegerField()
    Cargo = models.CharField(max_length=20)
    Usuario = models.CharField(max_length=10, unique=True)
    Contrasena = models.CharField(max_length=60)

    def __str__(self):
        return self.Id_Empleado
