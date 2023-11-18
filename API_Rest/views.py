from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Producto, Servicio, Cuenta_Empleado
from openpyxl import Workbook
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Cuenta_Empleado

def productos(request):
    productos = Producto.objects.all()
    return render(request, "core/productos.html", {"productos": productos})

def crud_productos(request):
    productos = Producto.objects.all()
    return render(request, "core/crud_productos.html", {"productos": productos})

def crud_empleados(request):
    cuenta_empleado = Cuenta_Empleado.objects.all()
    return render(request, "core/crud_cuentas.html", {"cuenta_empleado": cuenta_empleado})

def registrarEmpleado(request):
    Id_Empleado = request.POST["txtId_Empleado"]
    Primer_Nombre = request.POST["txtPrimer_nombre_Empleado"]
    Segundo_Nombre = request.POST["txtSegundo_nombre_Empleado"]
    Primer_Apellido = request.POST["txtPrimer_Apellido"]
    Segundo_Apellido = request.POST["txtSegundo_Apellido"]
    Direccion = request.POST["txtDireccion"]
    Edad = request.POST["txtEdad"]
    Cargo = request.POST["txtCargo"]

    cuenta_empleado = Cuenta_Empleado()
    cuenta_empleado.Id_Empleado = Id_Empleado
    cuenta_empleado.Primer_Nombre = Primer_Nombre
    cuenta_empleado.Segundo_Nombre = Segundo_Nombre
    cuenta_empleado.Primer_Apellido = Primer_Apellido
    cuenta_empleado.Segundo_Apellido = Segundo_Apellido
    cuenta_empleado.Direccion = Direccion
    cuenta_empleado.Edad = Edad 
    cuenta_empleado.Cargo = Cargo 

    cuenta_empleado.save()

    return redirect(reverse("crud_cuentas"))
def productos(request):
    # Consulta todos los productos desde el modelo Producto
    productos = Producto.objects.all()

    return render(request, 'core/productos.html', {"productos": productos})

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
    cuenta_empleado = Cuenta_Empleado.objects.all()
    return render(request, "core/crud_cuentas.html", {"cuenta_empleado": cuenta_empleado})


def productos(request):
    # Consulta todos los productos desde el modelo Producto
    productos = Producto.objects.all()
    return render(request, 'core/productos.html', {"productos": productos})


def perfil(request):
    return render(request, "core/perfil.html")


def servicios(request):
    # Consulta todos los servicios desde el modelo Servicio
    servicios = Servicio.objects.all()

    return render(request, 'core/servicios.html', {"servicios": servicios})


def pedidos(request):
    return render(request, "core/pedidos.html")

def generar_informe(request):
    # Lógica para obtener datos de productos, servicios y cuentas
    productos = Producto.objects.all()
    servicios = Servicio.objects.all()
    cuentas = Cuenta_Empleado.objects.all()

    # Crear un libro de Excel
    wb = Workbook()

    # Crear hojas para productos, servicios y cuentas
    ws_productos = wb.create_sheet(title="Productos")
    ws_servicios = wb.create_sheet(title="Servicios")
    ws_cuentas = wb.create_sheet(title="Cuentas")

    # Escribir datos en las hojas
    for producto in productos:
        ws_productos.append([producto.Id_Producto, producto.Nombre_Producto, producto.stock_Producto, producto.descripcion_Producto, producto.Precio_Producto, producto.Categoria_Producto, producto.Marca_Producto, producto.Proveedor_Producto])

    for servicio in servicios:
        ws_servicios.append([servicio.Id_Servicio, servicio.Nombre_Servicio, servicio.Tipo_Servicio, servicio.Precio_Servicio, servicio.Personal_cargo])

    for cuenta in cuentas:
        ws_cuentas.append([cuenta.Id_Empleado, cuenta.Primer_Nombre, cuenta.Segundo_Nombre, cuenta.Primer_Apellido, cuenta.Segundo_Apellido, cuenta.Direccion, cuenta.Edad, cuenta.Cargo])

    # Crear una respuesta de Django para el archivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=informe.xlsx'

    # Guardar el libro de Excel en la respuesta
    wb.save(response)

    return response

def login(request):
    if request.method == "POST":
        username = request.POST.get("txtIdEmp")
        password = request.POST.get("txtPasswordEmp")

        try:
            # Buscar al usuario en la base de datos
            empleado = Cuenta_Empleado.objects.get(Id_Empleado=username)

            # Verificar la contraseña
            if check_password(password, empleado.Contraseña):
                if empleado.Cargo == "cliente":
                    # Usuario es cliente, redirigir al index
                    return redirect("index")
                else:
                    # Usuario no es cliente, mostrar mensaje de denegación
                    messages.error(request, 'Acceso denegado para no clientes.')
            else:
                # Contraseña incorrecta
                messages.error(request, 'Contraseña incorrecta.')
        except Cuenta_Empleado.DoesNotExist:
            # Usuario no encontrado
            messages.error(request, 'Usuario no encontrado.')

    return render(request, "core/login.html")