from django.shortcuts import render, redirect
from django.urls import reverse
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


def registrarProductos(request):
    id_producto = request.POST["txtId_Producto"]
    nombre_producto = request.POST["txtNombre_Producto"]
    stock_producto = request.POST["txtstock_Producto"]
    descripcion_producto = request.POST["txtdescripcion_Producto"]
    precio = request.POST["txtPrecio_Producto"]
    categoria = request.POST["txtCategoria_Producto"]
    Marca = request.POST["txtMarca_Producto"]
    Proveedor = request.POST["txtProveedor_Producto"]

    producto = Producto()
    producto.Id_Producto = id_producto
    producto.Nombre_Producto = nombre_producto
    producto.stock_Producto = stock_producto
    producto.descripcion_Producto = descripcion_producto
    producto.Precio_Producto = precio
    producto.Categoria_Producto = categoria
    producto.Marca_Producto = Marca
    producto.Proveedor_Producto = Proveedor

    producto.save()

    return redirect(reverse("crud_productos"))


def eliminarProducto(request, Id_Producto):
    producto = Producto.objects.get(Id_Producto=Id_Producto)
    producto.delete()

    return redirect(reverse("crud_productos"))


def edicionProducto(request, Id_Producto):
    producto = Producto.objects.get(Id_Producto=Id_Producto)
    return render(request, "core/edicionProducto.html", {"producto": producto})


def EditarProductos(request):
    id_producto = request.POST["txtId_Producto"]
    nombre_producto = request.POST["txtNombre_Producto"]
    stock_producto = request.POST["txtstock_Producto"]
    descripcion_producto = request.POST["txtdescripcion_Producto"]
    precio = request.POST["txtPrecio_Producto"]
    categoria = request.POST["txtCategoria_Producto"]
    Marca = request.POST["txtMarca_Producto"]
    Proveedor = request.POST["txtProveedor_Producto"]

    producto = Producto.objects.get(Id_Producto=id_producto)
    producto = Producto()
    producto.Id_Producto = id_producto
    producto.Nombre_Producto = nombre_producto
    producto.stock_Producto = stock_producto
    producto.descripcion_Producto = descripcion_producto
    producto.Precio_Producto = precio
    producto.Categoria_Producto = categoria
    producto.Marca_Producto = Marca
    producto.Proveedor_Producto = Proveedor
    producto.save()

    return redirect(reverse("crud_productos"))


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
