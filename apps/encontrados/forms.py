from django import forms
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro


class PublicacionForm(forms.ModelForm):
   
   class Meta:
      model = Publicacion
      fields = [
         'observaciones'
      ]
      widgets = {
         'observaciones': forms.TextInput(attrs= {'class': 'form-control'}),
      }

class MascotaForm(forms.ModelForm):
   
   class Meta:
      model = Mascota
      exclude = [
         'id',
         'id_dueño',
      ]
      widgets = {
         'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
         'familia': forms.TextInput(attrs= {'class': 'form-control'}),
         'raza': forms.TextInput(attrs= {'class': 'form-control'}),
         'especie': forms.TextInput(attrs= {'class': 'form-control'}),
         'sexo': forms.TextInput(attrs= {'class': 'form-control'}),
         'color': forms.TextInput(attrs= {'class': 'form-control'}),
         'otro_dato': forms.TextInput(attrs= {'class': 'form-control'}),
         'edad': forms.NumberInput(attrs= {'class': 'form-control'}),
         'tamaño': forms.NumberInput(attrs= {'class': 'form-control'}),
         'fotos': forms.FileInput(attrs= {'class': 'form-control'}),
      }
      
class UbicacionForm(forms.ModelForm):
   
   class Meta:
      model = Ubicacion
      exclude = [
         'id',
      ]
      widgets = {
         'localidad': forms.TextInput(attrs= {'class': 'form-control'}),
         'barrio': forms.TextInput(attrs= {'class': 'form-control'}),
         'entre_calles': forms.TextInput(attrs= {'class': 'form-control'}),
         'numero': forms.TextInput(attrs= {'class': 'form-control'}),
         'calle': forms.TextInput(attrs= {'class': 'form-control'}),
         'otros_datos': forms.TextInput(attrs= {'class': 'form-control'}),
      }

class EncontroForm(forms.ModelForm):
  
   class Meta:
      model = Encontro
      fields = [
         'cuida',
         'fecha_limite',
         ]
      labels = {
         'cuida': 'Lo esta cuidando.?'
      }