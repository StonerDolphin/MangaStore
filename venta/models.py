from django.db import models

# Create your models here.
class Manga(models.Model):
    # Campos del modelo
    id_manga = models.CharField(primary_key = True, max_length = 10)
    titulo            = models.CharField(max_length  = 100)
    autor             = models.CharField(max_length  = 100)
    id_genero         = models.ForeignKey('genero', on_delete = models.CASCADE)
    fecha_publicacion = models.DateField()
    sinopsis          = models.TextField()

    def __str__(self):
        return self.titulo

class genero(models.Model):
    id_genero   = models.CharField(primary_key   =  True, max_length = 10)
    nomb_genero = models.CharField(max_length = 100)

    def __str__(self):
        return self.nomb_genero