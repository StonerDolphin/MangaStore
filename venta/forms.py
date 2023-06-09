from django import forms

from venta.models import cliente


class ClienteForm(forms.ModelForm):
	class Meta:
		model = cliente
		fields = '__all__'