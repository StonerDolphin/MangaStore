from django import forms
from .models import Genero,Editorial

class GeneroForm(forms.Form)
    genero = forms.ModelChoiceField(queryset=Genero.objects.all())