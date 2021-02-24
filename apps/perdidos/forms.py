from django import forms
from . import models 


class FormularioPublicacion(forms.ModelForm):
	class Meta:
		model = models.Publicacion
		fields = ('id_usuario', 'id_mascota', 'id_ubicacion', 'observaciones')

		widgets = {
			#'id_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar un título'}),
			#'id_mascota': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder'}),
			'id_ubicacion': forms.Select(choices=models.Ubicacion.lista_localidades, attrs={'class': 'form-select'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insertar texto interesante...'}),
		}