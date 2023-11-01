from django.shortcuts import render, redirect

# Create your views her.
def login(request):
    return render(request, "core/login.html")

def log_out(request):
     return render(request,"core/login.html")

def registro(request):
    return render(request, "core/registro.html")

def LoginEmpleados(request):
    return render(request, "core/LoginEmpleados.html")

def MenuEmpleados(request):
    return render(request, "core/MenuEmpleados.html")

def index(request):
    return render(request, "core/index.html")

