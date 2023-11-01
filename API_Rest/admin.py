from django.contrib import admin
from .models import Producto, Servicio, Cuenta_Empleado

# Register your models here.
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Cuenta_Empleado)
