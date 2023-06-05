from django.contrib import admin
from .models import genero,editorial,region,comuna,cliente,manga

# Register your models here.

admin.site.register(genero)
admin.site.register(editorial)
admin.site.register(region)
admin.site.register(comuna)
admin.site.register(cliente)
admin.site.register(manga)
