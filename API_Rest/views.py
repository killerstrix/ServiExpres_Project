from django.shortcuts import render, redirect
from .models import Producto


# Create your views her.
def login(request):
    return render(request, "core/login.html")


def log_out(request):
    return render(request, "core/login.html")


def registro(request):
    return render(request, "core/registro.html")


def LoginEmpleados(request):
    return render(request, "core/LoginEmpleados.html")


def MenuEmpleados(request):
    return render(request, "core/MenuEmpleados.html")


def index(request):
    return render(request, "core/index.html")


def crud_productos(request):
    productos = Producto.objects.all()
    return render(request, "core/crud_productos.html", {"productos": productos})


def crud_Servicios(request):
    return render(request, "core/crud_Servicios.html")


def crud_cuentas(request):
    return render(request, "core/crud_cuentas.html")


def Generar_Informes(request):
    return render(request, "core/Generar_Informes.html")


def productos(request):
    return render(request, "core/productos.html")


def perfil(request):
    return render(request, "core/perfil.html")


def servicios(request):
    return render(request, "core/servicios.html")


def pedidos(request):
    return render(request, "core/pedidos.html")
