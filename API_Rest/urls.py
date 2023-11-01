from django.urls import path
from . views import login, registro, LoginEmpleados, index, MenuEmpleados

urlpatterns=[
    path('', login, name="login"),
    path('registro', registro, name="registro"),
    path('LoginEmpleados', LoginEmpleados, name="LoginEmpleados"),
    path('MenuEmpleados', MenuEmpleados, name="MenuEmpleados"),
    path('index', index, name="index"),
]