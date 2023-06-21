from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import Genero,Editorial,Region,Comuna,Cliente,Manga
from django.contrib import messages
from django.db import IntegrityError
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

def signup(request):
    context = {}
    print('registro')
    if request.method == 'POST':
        print('request.POST')
        print(request.POST)
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        if password == password2:
            try:
                print('pre')
                user = User.objects.create_user(username=usuario, password=password, email=correo, first_name=nombre)
                user.save()

                c = Cliente.objects.create(user=user, telefono=telefono, nombre=nombre, email=correo)
                c.save()

                messages.success(request, 'Cliente creado')
                context['success'] = True
                print('finish')
                return render(request, 'venta/registrarse.html', context)
            except Exception as e:
                print('e')
                print(e)
                return render(request, 'venta/registrarse.html', context)
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'venta/registrarse.html', context)
    else:
        return render(request, 'venta/registrarse.html', context)

def tienda(request):
    return render(request,'venta/tienda.html')

def crud(request):
    venta = Manga.objects.all()
    context ={'mangas':venta}
    return render(request,'venta/crudMangas.html', context)

def mangas(request):
    mangas = Manga.objects.all()
    return render(request, 'venta/crudMangas.html', {'mangas': mangas})

def lista_genero(request):
    lista_generos = Genero.objects.all() #select * from Genero
    context = {"generos":lista_generos}
    return render(request,'venta/crudMangas.html', context)

def lista_editoriales(request):
    lista_editoriales = Editorial.objects.all() #select * from Editorial
    context = {"editoriales":lista_editoriales}
    return render(request,'venta/crudMangas.html', context)


def registrarManga(request):

    if request.method != "POST":
        lista_generos = Genero.objects.all()
        lista_editoriales = Editorial.objects.all()
        context = {"generos":lista_generos,"editoriales":lista_editoriales}
        return render(request,'venta/agregarManga.html', context)
    else:

        id_manga = request.POST['txtId']
        titulo= request.POST['txtTitulo']
        nro_volumen= request.POST['nVolumen']
        precio= request.POST['nPrecio']
        autor = request.POST['txtAutor']
        stock = request.POST['nStock']
        fecha_publicacion = request.POST['dFecha']
        sinopsis = request.POST['txtSinopsis']
        generos = request.POST['genero']
        editoriales = request.POST['editorial']
        cover = request.POST['imagen']

        objGenero=Genero.objects.get(id_genero = generos)
        objEditorial=Editorial.objects.get(id_editorial = editoriales)
        objManga = Manga.objects.create(
            id_manga=id_manga, titulo=titulo, nro_volumen=nro_volumen,
            precio=precio, autor=autor, stock=stock, 
            fecha_publicacion=fecha_publicacion, sinopsis=sinopsis,
            id_genero=objGenero,id_editorial=objEditorial,cover=cover)
        objManga.save()
        lista_generos = Genero.objects.all()
        lista_editoriales = Editorial.objects.all()
        context = {"generos":lista_generos,"editoriales":lista_editoriales}
        messages.success(request, '¡Manga registrado!')
        return render(request,'venta/agregarManga.html', context)

def buscar_manga(request,pk):
    if pk != "":
        manga = Manga.objects.get(id_manga=pk)
        lista_generos = Genero.objects.all()
        lista_editoriales = Editorial.objects.all() 
        context = {"manga":manga, "generos":lista_generos,"editoriales":lista_editoriales}
        return render(request,'venta/modificarMangas.html', context)
    else:
        mensaje = "El alumno NO existe"
        context = {"mensaje":mensaje}
        return render(request,'venta/index.html', context)

def modificarMangas(request):
    if request.method == "POST":
        
        id_manga = request.POST['txtId']
        titulo= request.POST['txtTitulo']
        nro_volumen= request.POST['nVolumen']
        precio= request.POST['nPrecio']
        autor = request.POST['txtAutor']
        stock = request.POST['nStock']
        fecha_publicacion = request.POST['dFecha']
        sinopsis = request.POST['txtSinopsis']
        generos = request.POST['genero']
        editoriales = request.POST['editorial']

        
        objGenero = Genero.objects.get(id_genero = generos)
        objEditorial=Editorial.objects.get(id_editorial = editoriales)
        
        objManga = Manga()
        objManga.id_manga          = id_manga
        objManga.titulo            = titulo
        objManga.nro_volumen       = nro_volumen
        objManga.precio            = precio
        objManga.autor             = autor
        objManga.stock             = stock
        objManga.fecha_publicacion = fecha_publicacion
        objManga.sinopsis          = sinopsis
        objManga.id_genero         = objGenero
        objManga.id_editorial      = objEditorial
            
        objManga.save() #update
      
        lista_generos = Genero.objects.all()
        lista_editoriales = Editorial.objects.all()
        context = {"generos":lista_generos,"editoriales":lista_editoriales, "manga":objManga}
        messages.success(request, '¡Manga actualizado!')
        return render(request,'venta/modificarMangas.html', context)
    else:
        mangas = Manga.objects.all()
        context = {"mangas":mangas}
        return render(request,'venta/crudMangas.html', context)



def eliminarManga(request, pk):
    try:
        manga = Manga.objects.get(id_manga=pk)
        manga.delete()
        mensaje = "El manga se eliminó"
        mangas = Manga.objects.all()
        context = {"mangas":mangas,"mensaje":mensaje}
        return render(request,'venta/crudMangas.html', context)
    except:
        mensaje = "El manga no se eliminó"
        mangas = Manga.objects.all()
        context = {"mangas":mangas,"mensaje":mensaje}
        return render(request,'venta/crudMangas.html', context)
