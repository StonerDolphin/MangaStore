from django.shortcuts import render
# Create your views here.
def inicio(request):
    context={}
    return render (request,'venta/index.html', context)

def compra(request):
    return render (request,'venta/compra.html')

def login(request):
    return render(request,'venta/login.html')

def producto(request):
    return render(request,'venta/producto.html')

def progreso(request):
    return render(request,'venta/progreso.html')

def registrarse(request):
    return render(request,'venta/registrarse.html')

def tienda(request):
    return render(request,'venta/tienda.html')

