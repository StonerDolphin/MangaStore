from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from venta.models import Cliente
from django.contrib import messages

# Create your views here.
def inicio(request):
    context={}
    return render (request,'venta/index.html', context)

def compra(request):
    return render (request,'venta/compra.html')

def signin(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'El usuario no existe')
            return render(request,'venta/login.html')

        messages.success(request, 'Exito')
        login(request, user)
        return redirect('index')
    else:
        return render(request,'venta/login.html')

def producto(request):
    return render(request,'venta/producto.html')

def progreso(request):
    return render(request,'venta/progreso.html')



def registrarse(request):

    context = {}

    if request.method == 'POST':
        usuario       = request.POST.get('usuario')
        password      = request.POST.get('password')
        password2     = request.POST.get('password2')
        nombre        = request.POST.get('nombre')
        correo        = request.POST.get('correo')
        telefono      = request.POST.get('telefono')

        if password == password2:

            user = User.objects.create_user(username=usuario, password=password, email=correo, first_name=nombre)
            user.save()

            c = Cliente.objects.create(user=user, telefono=telefono, nombre=nombre, email=correo)
            c.save()

            messages.success(request, 'Cliente creado')
            context['success'] = True

            return render(request, 'venta/registrarse.html', context)
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'venta/registrarse.html', context)
    else:
        return render(request,'venta/registrarse.html', context)

def tienda(request):
    return render(request,'venta/tienda.html')