from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Producto, Servicio


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
    servicios = Servicio.objects.all()
    return render(request, "core/crud_Servicios.html", {"servicios": servicios})


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


def registrarServicios(request):
    id_servicio = request.POST["txtId_Servicio"]
    nombre_servicio = request.POST["txtNombre_Servicio"]
    tipo_servicio = request.POST["txtTipo_Servicio"]
    precio_servicio = request.POST["txtPrecio_Servicio"]
    personal_cargo = request.POST["txtPersonal_cargo"]

    servicio = Servicio()
    servicio.Id_Servicio = id_servicio
    servicio.Nombre_Servicio = nombre_servicio
    servicio.Tipo_Servicio = tipo_servicio
    servicio.Precio_Servicio = precio_servicio
    servicio.Personal_cargo = personal_cargo

    servicio.save()

    return redirect(reverse("crud_Servicios"))


def eliminarProducto(request, Id_Producto):
    producto = Producto.objects.get(Id_Producto=Id_Producto)
    producto.delete()

    return redirect(reverse("crud_productos"))


def EliminarServicio(request, Id_Servicio):
    servicio = Servicio.objects.get(Id_Servicio=Id_Servicio)
    servicio.delete()

    return redirect(reverse("crud_Servicios"))


def edicionProducto(request, Id_Producto):
    producto = Producto.objects.get(Id_Producto=Id_Producto)
    return render(request, "core/edicionProducto.html", {"producto": producto})


def edicionServicio(request, Id_Servicio):
    servicio = Servicio.objects.get(Id_Servicio=Id_Servicio)
    return render(request, "core/edicionServicio.html", {"servicio": servicio})


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


def EditarServicios(request):
    id_servicio = request.POST["txtId_Servicio"]
    nombre_servicio = request.POST["txtNombre_Servicio"]
    tipo_servicio = request.POST["txtTipo_Servicio"]
    precio_servicio = request.POST["txtPrecio_Servicio"]
    personal_cargo = request.POST["txtPersonal_cargo"]

    servicio = Servicio.objects.get(Id_Servicio=id_servicio)
    servicio = Servicio()
    servicio.Id_Servicio = id_servicio
    servicio.Nombre_Servicio = nombre_servicio
    servicio.Tipo_Servicio = tipo_servicio
    servicio.Precio_Servicio = precio_servicio
    servicio.Personal_cargo = personal_cargo
    servicio.save()

    return redirect(reverse("crud_Servicios"))


def crud_cuentas(request):
    return render(request, "core/crud_cuentas.html")


def productos(request):
    return render(request, "core/productos.html")


def perfil(request):
    return render(request, "core/perfil.html")


def servicios(request):
    return render(request, "core/servicios.html")


def pedidos(request):
    return render(request, "core/pedidos.html")
