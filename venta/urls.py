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
    path('signin',views.signin, name='signin'),
    path('producto',views.producto, name='producto'),
    path('progreso',views.progreso, name='progreso'),
    path('signup',views.signup, name='signup'),
    path('tienda',views.tienda, name='tienda'),
    path('crud',views.crud, name='crud'),
    path('generos',views.generos, name='generos'),
    path('mangas',views.mangas, name='mangas'),
    path('lista_editoreales',views.lista_editoriales, name='lista_editoreales'),
    path('registrarManga/', views.registrarManga),
    path('modificarMangas/<id>', views.modificarMangas),
    path('editarManga/', views.editarManga),
    path('eliminarManga/<codigo>', views.eliminarManga),
]
