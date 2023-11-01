from django.urls import path
from . views import login, registro, LoginEmpleados, index, MenuEmpleados,productos,perfil,servicios,pedidos

urlpatterns=[
    path('', login, name="login"),
    path('registro/', registro, name="registro"),
    path('LoginEmpleados/', LoginEmpleados, name="LoginEmpleados"),
    path('MenuEmpleados/', MenuEmpleados, name="MenuEmpleados"),
    path('index/', index, name="index"),
    path('registro/', registro, name="registro"),
    path('productos/', productos, name="productos"),
    path('perfil/', perfil, name="perfil"),
    path('servicios/', servicios, name="servicios"),
    path('pedidos/', pedidos, name="pedidos"),
    
]