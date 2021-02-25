from django import forms
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro


class PublicacionForm(forms.ModelForm):
   
   class Meta:
      model = Publicacion
      fields = [
         'observaciones'
      ]
      help_texts = {'observaciones': ''}

class MascotaForm(forms.ModelForm):
   
   class Meta:
      model = Mascota
      exclude = [
         'id',
         'id_dueño',
      ]
      # fields = [
      #    'nombre',
      #    'familia',
      #    'raza',
      #    'edad',
      #    'sexo',
      #    'fotos',
      #    'color',
      #    'tamaño',
      #    'otro_dato',
      # ]
      #help_texts = {field:'' for field in fields}
      
      
class UbicacionForm(forms.ModelForm):
   
   class Meta:
      model = Ubicacion
      exclude = [
         'id',
      ]
      # fields = [
      #    'localidad',
      #    'barrio',
      #    'entre_calles',
      #    'numero',
      #    'calle',
      #    'otros_datos',
      # ]

class EncontroForm(forms.ModelForm):
   
   class Meta:
      model = Encontro
      fields = [
         'cuida',
         'fecha_limite',
         ]

"""
class FormularioPublicacion(forms.ModelForm):
	class Meta:
		model = models.Publicacion
		fields = ('id_usuario', 'id_mascota', 'id_ubicacion', 'observaciones')

		widgets = {
			'id_usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insertar un título', 'type':'hidden'}),
			'id_mascota': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder','type':'hidden'}),
			'id_ubicacion': forms.Select(choices=models.Ubicacion.localidad, attrs={'class': 'form-select'},),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Insertar texto interesante...'}),
		}"""