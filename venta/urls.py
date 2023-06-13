"""
URL configuration for mangaStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='index'),
    path('compra',views.compra, name='compra'),
    path('login',views.login, name='login'),
    path('producto',views.producto, name='producto'),
    path('progreso',views.progreso, name='progreso'),
    path('registrarse',views.registrarse, name='registrarse'),
    path('tienda',views.tienda, name='tienda'),
    path('crud',views.crud, name='crud'),
    path('generos',views.lista_genero, name='generos'),
    path('mangas',views.mangas, name='mangas'),
    path('editoriales',views.lista_editoriales, name='editoriales'),
    path('registrarManga', views.registrarManga, name='registrarManga'),
    path('buscar_manga/<str:pk>',views.buscar_manga, name='buscar_manga'),
    path('modificarMangas', views.modificarMangas, name='modificarMangas'),
    path('eliminarManga/<str:pk>', views.eliminarManga, name='eliminarManga'),
]
