from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .models import Genero, Editorial, Region, Comuna, Cliente, Manga
from django.contrib import messages


# Create your views here.

def inicio(request):
    context = {}
    return render(request, 'venta/index.html', context)


def compra(request):
    return render(request, 'venta/compra.html')


def signin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is None:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Contraseña incorrecta')
            else:
                messages.error(request, 'El usuario no existe')
            return render(request, 'venta/login.html')

        messages.success(request, 'Exito')
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'venta/login.html')


def producto(request):
    return render(request, 'venta/producto.html')


def progreso(request):
    return render(request, 'venta/progreso.html')


def signup(request):
    context = {}

    if request.method == 'POST':
        usuario       = request.POST.get('usuario')
        password      = request.POST.get('password')
        password2     = request.POST.get('password2')
        nombre        = request.POST.get('nombre')
        correo        = request.POST.get('correo')
        telefono      = request.POST.get('telefono')

        if password == password2:
            try:
                user = User.objects.create_user(username=usuario, password=password, email=correo, first_name=nombre)
                user.save()

                c = Cliente.objects.create(user=user, telefono=telefono, nombre=nombre, email=correo)
                c.save()

                messages.success(request, 'Cliente creado')
                context['success'] = True

                return render(request, 'venta/registrarse.html', context)
            except Exception as e:
                context['error'] = str(e)
                return render(request, 'venta/registrarse.html', context)

        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'venta/registrarse.html')
    else:
        return render(request, 'venta/registrarse.html', context)


def tienda(request):
    return render(request, 'venta/tienda.html')


def crud(request):
    venta = Manga.objects.all()
    context = {'mangas': venta}
    return render(request, 'venta/crudMangas.html', context)


def mangas(request):
    mangas = Manga.objects.all()
    return render(request, 'venta/crudMangas.html', {'mangas': mangas})


def generos(request):
    generos = Genero.objects.all()
    return render(request, 'venta/crudMangas.html', {'generos': generos})


def lista_editoriales(request):
    lista_editoreales = Editorial.objects.all()  # select * from Editorial
    context = {"editoriales": lista_editoreales}
    return render(request, 'venta/crudMangas.html', context)


def registrarManga(request):
    id_manga = request.POST['txtId']
    titulo = request.POST['txtTitulo']
    nro_volumen = request.POST['nVolumen']
    precio = request.POST['nPrecio']
    autor = request.POST['txtAutor']
    stock = request.POST['nStock']
    fecha_publicacion = request.POST['dFecha']
    sinopsis = request.POST['txtSinopsis']
    generos = request.POST['genero']
    editoriales = request.POST['editorial']

    objGenero = Genero.objects.get(id_genero=generos)
    objEditorial = Editorial.objects.get(id_editorial=editoriales)
    manga = Manga.objects.create(
        id_manga=id_manga, titulo=titulo, nro_volumen=nro_volumen,
        precio=precio, autor=autor, stock=stock,
        fecha_publicacion=fecha_publicacion, sinopsis=sinopsis,
        id_genero=objGenero, id_editorial=objEditorial)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')


def modificarMangas(request, id_manga):
    manga = Manga.objects.get(id_manga=id_manga)
    return render(request, "modificarMangas.html", {"venta": manga})


def editarManga(request):
    id_manga = request.POST['txtId']
    titulo = request.POST['txtTitulo']
    nro_volumen = request.POST['nVolumen']
    precio = request.POST['nPrecio']
    autor = request.POST['txtAutor']
    stock = request.POST['nStock']
    fecha_publicacion = request.POST['txtFecha']
    sinopsis = request.POST['txtSinopsis']

    manga = Manga.objects.get(id_manga=id_manga)
    manga.titulo = titulo
    manga.nro_volumen = nro_volumen
    manga.precio = precio
    manga.autor = autor
    manga.stock = stock
    manga.fecha_publicacion = fecha_publicacion
    manga.sinopsis = sinopsis
    manga.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/')


def eliminarManga(request, id_manga):
    manga = Manga.objects.get(id_manga=id_manga)
    manga.delete()

    messages.success(request, '¡Curso eliminado!')

    return redirect('/')
