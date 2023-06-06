from django.shortcuts import render,redirect
from .models import Genero,Editorial,Region,Comuna,Cliente,Manga
from django.contrib import messages
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

def crud(request):
    venta = Manga.objects.all()
    context ={'mangas':venta}
    return render(request,'venta/crudMangas.html', context)

def home(request):
    mangasListados = Manga.objects.all()
    messages.success(request, '¡Cursos listados!')
    return render(request, "crudMangas.html", {"cursos": mangasListados})

def registrarManga(request):
    id_manga = request.POST['txtId']
    titulo= request.POST['txtTitulo']
    nro_volumen= request.POST['nVolumen']
    precio= request.POST['nPrecio']
    autor = request.POST['txtAutor']
    stock = request.POST['nStock']
    fecha_publicacion = request.POST['txtFecha']
    sinopsis = request.POST['txtSinopsis']
    manga = Manga.objects.create(
        id_manga=id_manga, titulo=titulo, nro_volumen=nro_volumen, precio=precio, autor=autor, stock=stock, fecha_publicacion=fecha_publicacion, sinopsis=sinopsis)
    messages.success(request, '¡Curso registrado!')
    return redirect('/')

def modificarMangas(request, id_manga):
    manga= Manga.objects.get(id_manga=id_manga)
    return render(request, "modificarMangas.html", {"venta": manga})

def editarManga(request):
    id_manga = request.POST['txtId']
    titulo= request.POST['txtTitulo']
    nro_volumen= request.POST['nVolumen']
    precio= request.POST['nPrecio']
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