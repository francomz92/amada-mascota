from django import forms
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro, lista_especies, lista_localidades
from django.contrib.auth.models import User

# class PublicacionForm(forms.ModelForm):

#    class Meta:
#       model = Publicacion
#       exclude = {
#          'id_usuario',
#          'id_mascota',
#          'id_ubicacion',
#       }
#       widgets = {
#          'observaciones': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
#       }
      
class MascotaForm(forms.ModelForm):

   class Meta:
      model = Mascota
      fields = '__all__'
      widgets = {
         'id_dueño': forms.Select(attrs= {'name': 'id_dueño', 'hidden': '',}),
         'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
         'familia': forms.TextInput(attrs= {'class': 'form-control'}),
         'raza': forms.TextInput(attrs= {'class': 'form-control'}),
         'especie': forms.Select(attrs= {'class': 'form-control'}),
         'sexo': forms.Select(attrs= {'class': 'form-control'}),
         'color': forms.TextInput(attrs= {'class': 'form-control'}),
         'otro_dato': forms.Textarea(attrs= {'class': 'form-control', 'rows': 5, 'style': 'resize: none;'}),
         'edad': forms.NumberInput(attrs= {'class': 'form-control', 'maxlength': '2'}),
         'tamaño': forms.Select(attrs= {'class': 'form-control'}),
         'fotos': forms.FileInput(attrs= {'class': 'form-control'}),
      }
      labels = {
         'id_dueño': '',
         'nombre': 'Mascota*',
         'familia': 'Familia*',
         'otro_dato': 'Alguna descripción adicional',
         'edad': 'Edad aproximada*',
         'especie': 'Especie*',
         'raza': 'Raza*',
         'tamaño': 'Tamaño*',
         'sexo': 'Sexo*',
         'fotos': 'Foto*',
      }
      help_texts = {
         'familia': 'Indique la familia de la mascota en caso de conocerla',
         'especie': '',
      }
      
class UbicacionForm(forms.ModelForm):
   
   class Meta:
      model = Ubicacion
      fields = '__all__'
      widgets = {
         'localidad': forms.Select(attrs= {'class': 'form-control'}),
         'barrio': forms.TextInput(attrs= {'class': 'form-control'}),
         'entre_calles': forms.TextInput(attrs= {'class': 'form-control'}),
         'numero': forms.NumberInput(attrs= {'class': 'form-control', 'maxlength': '2'}),
         'calle': forms.TextInput(attrs= {'class': 'form-control'}),
         'otros_datos': forms.Textarea(attrs= {'class': 'form-control', 'rows': 2, 'style': 'resize: none;'}),
      }
      labels = {
         'localidad': 'Localidad*',
         'barrio': 'Barrio*',
         'calle': 'Calle*',
         'numero': 'Número*',
         'otros_datos': 'Alguna referencia*',
      }

class EncontroForm(forms.ModelForm):
   
   class Meta:
      model = Encontro
      exclude = [
         'id_usuario',
         'id_mascota',
         'id_ubicacion',
         'fecha_entrega',
      ]
      widgets = {
         'cuida': forms.Select(choices= Encontro.en_transito, attrs= {'class': 'form-control', 'name': 'cuida'}),
         'fecha_limite': forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'mm/dd/aaaa'}),
         'fecha_evento': forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'mm/dd/aaaa'}),
         'observaciones': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
      }
      labels = {
         'observaciones': 'Observaciones*',
         'fecha_evento': 'Cuándo lo encontro.?*',
         'cuida': 'Lo esta cuidando.?*',
         'fecha_limite': 'Hasta cuándo.?',
      }
      help_texts = {
         'fecha_limite': 'En caso de cuidarlo indique hasta cuando',
      }