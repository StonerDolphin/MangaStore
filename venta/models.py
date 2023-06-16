from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Genero(models.Model):
    # Campos del modelo
    id_genero   = models.CharField(primary_key=True, max_length = 10)
    nomb_genero = models.CharField(max_length = 100, blank=False, null=False)
    def __str__(self):
        return str(self.nomb_genero)


class Editorial(models.Model):
    # Campos del modelo
    id_editorial   = models.AutoField(primary_key   =  True)
    nomb_editorial = models.CharField(max_length = 100, blank=False, null=False)
    def __str__(self):
        return str(self.nomb_editorial)

class Region(models.Model):
    # Campos del modelo
    id_region   = models.AutoField(primary_key   =  True)
    nomb_region = models.CharField(max_length = 100)
    def __str__(self):
        return str(self.nomb_region)

class Comuna(models.Model):
    # Campos del modelo
    id_comuna   = models.AutoField(primary_key   =  True)
    nomb_comuna = models.CharField(max_length = 100)
    id_region   = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='id_region')
    def __str__(self):
        return str(self.nomb_comuna)

class Cliente(models.Model):
    # Campos del modelo
    user      = models.OneToOneField(User  ,default='null', on_delete = models.CASCADE, primary_key = True)
    nombre    = models.CharField(max_length = 100)
    email     = models.EmailField(unique    = True)
    telefono  = models.CharField(max_length = 20)


    def __str__(self):
        return str(self.nombre)
class Manga(models.Model):
    # Campos del modelo
    id_manga          = models.CharField(primary_key = True, max_length = 10)
    titulo            = models.CharField(max_length = 100)
    nro_volumen       = models.CharField(max_length = 10)
    precio            = models.CharField(max_length = 100)
    autor             = models.CharField(max_length = 100)
    stock             = models.CharField(max_length=100, null=True)
    cover             = models.ImageField(default = 'null', upload_to = 'manga')
    sinopsis          = models.TextField()
    id_genero         = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='id_genero')
    id_editorial      = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='id_editorial')
    def __str__(self):
        return str(self.titulo)+" "+str(self.nro_volumen)


