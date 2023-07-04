import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Genero(models.Model):
    # Campos del modelo
    id_genero = models.CharField(primary_key = True, max_length = 10)
    nomb_genero = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.nomb_genero)

class Editorial(models.Model):
    # Campos del modelo
    id_editorial = models.CharField(primary_key = True, max_length = 10)
    nomb_editorial = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.nomb_editorial)

class Region(models.Model):
    # Campos del modelo
    id_region = models.CharField(primary_key = True, max_length = 10)
    nomb_region = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.nomb_region)

class Comuna(models.Model):
    # Campos del modelo
    id_comuna = models.CharField(primary_key = True, max_length = 10)
    nomb_comuna = models.CharField(max_length = 100)
    id_region = models.ForeignKey(Region, on_delete = models.CASCADE, db_column = 'id_region')
    def __str__(self):
        return str(self.nomb_comuna)


class Cliente(models.Model):
    # Campos del modelo
    user = models.OneToOneField(User, default = 'null', on_delete = models.CASCADE, primary_key = True)
    nombre = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    telefono = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.nombre)

class Manga(models.Model):
    # Campos del modelo
    id_manga = models.CharField(primary_key = True, max_length = 10)
    titulo = models.CharField(max_length = 100)
    nro_volumen = models.CharField(max_length = 10)
    precio = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    stock = models.CharField(max_length = 100, null = True)
    cover = models.ImageField(default = 'null', upload_to = 'manga')
    fecha_publicacion = models.DateField(blank=False, null=False)
    sinopsis = models.TextField()
    id_genero = models.ForeignKey(Genero, on_delete = models.CASCADE, db_column = 'id_genero')
    id_editorial = models.ForeignKey(Editorial, on_delete = models.CASCADE, db_column = 'id_editorial')
    def __str__(self):
        return str(self.titulo) + " " + str(self.nro_volumen)

class Carrito(models.Model):
    # Campos del modelo
    id_carrito = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'user_id')
    def __str__(self):
        return str(self.id_carrito)

class CarritoItem(models.Model):
    manga = models.ForeignKey(Manga, on_delete = models.CASCADE, related_name='items')
    carrito = models.ForeignKey(Carrito, on_delete = models.CASCADE, related_name='carritoItems')
    cantidad = models.IntegerField(default=0)
    def __str__(self):
        return self.manga.titulo

class Orden(models.Model):
    # Campos del modelo
    nro_recibo = models.CharField(primary_key = True, max_length = 10)
    direccion = models.CharField(max_length = 100)
    cod_postal = models.CharField(max_length = 10)
    id_comuna = models.ForeignKey(Comuna, on_delete = models.CASCADE, db_column = 'id_comuna')
    def __str__(self):
        return str(self.nro_recibo)

class Orden_manga(models.Model):
    # Campos del modelo
    id_orden_manga = models.CharField(primary_key = True, max_length = 10)
    id_manga = models.ForeignKey(Manga, on_delete = models.CASCADE, db_column = 'id_manga')
    nro_recibo = models.ForeignKey(Orden, on_delete = models.CASCADE, db_column = 'nro_recibo')
    def __str__(self):
        return str(self.nro_recibo)

class Pago_orden(models.Model):
    # Campos del modelo
    id_pago_orden = models.CharField(primary_key = True, max_length = 10)
    nro_tarjeta = models.CharField(max_length = 100)
    estado_pago = models.CharField(max_length = 100)
    user_id = models.ForeignKey(Cliente, on_delete = models.CASCADE, db_column = 'user_id')
    nro_recibo = models.ForeignKey(Orden, on_delete = models.CASCADE, db_column = 'nro_recibo')
    def __str__(self):
        return str(self.nro_recibo)

