from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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

def producto(request):
    return render(request, 'venta/producto.html')

def progreso(request):
    return render(request, 'venta/progreso.html')

def signup(request):    
    context = {}
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')

        if password == password2:
            try:
                user = User.objects.create_user(username=correo, password=password, email=correo,
                                                first_name=nombre, last_name=usuario)
                user.save()

                c = Cliente.objects.create(user=user, telefono=telefono, nombre=nombre, email=correo)
                c.save()

                messages.success(request, 'Cliente creado')
                context['success'] = True

                return render(request, 'venta/registrarse.html', context)
            except Exception as e:
                print(e)
                return render(request, 'venta/registrarse.html', context)
        else:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, 'venta/registrarse.html', context)
    else:
        return render(request, 'venta/registrarse.html', context)

def signin(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        password = request.POST['password']
        user = authenticate(request, username = correo, password = password)
        if user is None:
            messages.error(request, 'El usuario no existe')
            return render(request, 'venta/login.html')
        else:
            messages.success(request, 'Exito')
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'venta/login.html')

@login_required
def listaUsuario(request):
    clientes = Cliente.objects.all()

    context = {"users": clientes}
    return render(request, 'venta/crudClientes.html',context)
@login_required
def crearUsuario(request):
    if request.method == "POST":
        usuario  = request.POST['usuario']
        nombre   = request.POST['nombre']
        correo   = request.POST['correo']
        telefono = request.POST['telefono']
        password = request.POST['password']

        # Verificar si el correo electrónico ya está registrado.
        if User.objects.filter(email=correo).exists():
            messages.add_message(request, messages.ERROR, '¡Este correo electrónico ya está en uso!')
            return render(request, 'venta/agregarUsuario.html')

        objUser = User.objects.create_user(username=correo, password=password, first_name= nombre,
                                           last_name=usuario, email=correo)
        objUser.save()

        objclient = Cliente.objects.create(user=objUser, telefono=telefono, nombre=nombre, email=correo)
        objclient.save()

        messages.success(request, '¡Usuario Creado!')
        return render(request, 'venta/agregarUsuario.html')
    else:
        return render(request, 'venta/agregarUsuario.html')
@login_required
def eliminarUsuario(request, pk):
    try:
        user = User.objects.get(id = pk)
        user.delete()
        return redirect('clientes')
    except:
        messages.add_message(request, messages.ERROR, 'No se pudo eliminar este usuario')
        return redirect('clientes')
@login_required
def buscarUsuario(request, pk):
    if pk != "":
        user = User.objects.get(id=pk)
        context = {"usuarios": user}
        return render(request, 'venta/modificarUsuario.html', context)
    else:
        mensaje = "el Usuario no existe"
        context = {"mensaje": mensaje}
        return render(request,'venta/modificarUsuario.html',context)
@login_required
def modificarUsuario(request, pk):
    if request.method == "POST":
        usuario  = request.POST['usuario']
        nombre   = request.POST['nombre']
        correo   = request.POST['correo']
        telefono = request.POST['telefono']

        try:
            # Obtener la instancia de User y Cliente existente
            objUser = User.objects.get(id=pk)
            objCli = Cliente.objects.get(user=objUser)

            # Actualizar los atributos de las instancias
            objUser.first_name = nombre
            objUser.last_name  = usuario
            objUser.username   = correo

            objCli.nombre   = nombre
            objCli.email    = correo
            objCli.telefono = telefono

            # Guardar las instancias actualizadas
            objUser.save()
            objCli.save()
        except (User.DoesNotExist, Cliente.DoesNotExist):
            messages.error(request,'Usuario o cliente no encontrado')
            return render(request, 'venta/modificarUsuario.html')

        messages.success(request,'Usuario actualizado')
        return redirect('clientes')
    else: # GET
        user = User.objects.get(id=pk)
        cliente = Cliente.objects.get(user=user)
        obj = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'nombre': cliente.nombre,
            'email': cliente.email,
            'telefono': cliente.telefono
        }
        context = {"user": obj}
        return render(request, 'venta/modificarUsuario.html', context)

def tienda(request):
    return render(request,'venta/tienda.html')
@login_required
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

@login_required
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
@login_required
def buscar_manga(request,pk):
    if pk != "":
        manga = Manga.objects.get(id_manga=pk)
        lista_generos = Genero.objects.all()
        lista_editoriales = Editorial.objects.all() 
        context = {"manga":manga, "generos":lista_generos,"editoriales":lista_editoriales}
        return render(request,'venta/modificarMangas.html', context)
    else:
        mensaje = "El manga NO existe"
        context = {"mensaje":mensaje}
        return render(request,'venta/index.html', context)
@login_required
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


@login_required
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
