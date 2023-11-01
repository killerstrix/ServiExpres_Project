from django.urls import path
from . views import login, registro, LoginEmpleados, index, MenuEmpleados, crud_productos, crud_Servicios, crud_cuentas, Generar_Informes

urlpatterns=[
    path('', login, name="login"),
    path('registro/', registro, name="registro"),
    path('LoginEmpleados/', LoginEmpleados, name="LoginEmpleados"),
    path('MenuEmpleados/', MenuEmpleados, name="MenuEmpleados"),
    path('index/', index, name="index"),
    path('crud_productos/', crud_productos, name="crud_productos"),
    path('crud_Servicios/', crud_Servicios, name="crud_Servicios"),
    path('crud_cuentas/', crud_cuentas, name="crud_cuentas"),
    path('Generar_Informes/', Generar_Informes, name="Generar_Informes"),
]