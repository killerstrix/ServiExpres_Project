from django.urls import path
from .views import (
    login,
    registro,
    LoginEmpleados,
    index,
    MenuEmpleados,
    productos,
    perfil,
    servicios,
    pedidos,
    crud_productos,
    registrarProductos,
    crud_Servicios,
    crud_cuentas,
    eliminarProducto,
    edicionProducto,
    EditarProductos,
    registrarServicios,
    EliminarServicio,
    edicionServicio,
    EditarServicios,
    registrarEmpleado,
    generar_informe,
)

urlpatterns = [
    path("", login, name="login"),
    path("registro/", registro, name="registro"),
    path("LoginEmpleados/", LoginEmpleados, name="LoginEmpleados"),
    path("MenuEmpleados/", MenuEmpleados, name="MenuEmpleados"),
    path("index/", index, name="index"),
    path("crud_productos/", crud_productos, name="crud_productos"),
    path("registrarProductos/", registrarProductos, name="registrarProductos"),
    path("eliminarProducto/<Id_Producto>", eliminarProducto, name="eliminarProducto"),
    path("edicionProducto/<Id_Producto>", edicionProducto, name="edicionProducto"),
    path("EditarProductos/", EditarProductos, name="EditarProductos"),
    path("crud_Servicios/", crud_Servicios, name="crud_Servicios"),
    path("registrarServicios/", registrarServicios, name="registrarServicios"),
    path("EliminarServicio/<Id_Servicio>", EliminarServicio, name="EliminarServicio"),
    path("edicionServicio/<Id_Servicio>", edicionServicio, name="edicionServicio"),
    path("EditarServicios/", EditarServicios, name="EditarServicios"),
    path("crud_cuentas/", crud_cuentas, name="crud_cuentas"),
    path("registro/", registro, name="registro"),
    path("registrarEmpleado/", registrarEmpleado, name="registrarEmpleado"),
    path("productos/", productos, name="productos"),
    path("perfil/", perfil, name="perfil"),
    path("servicios/", servicios, name="servicios"),
    path("pedidos/", pedidos, name="pedidos"),
    path('generar_informe/', generar_informe, name='generar_informe'),
]
