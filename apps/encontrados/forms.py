from django import forms
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro, lista_especies, lista_localidades
from django.contrib.auth.models import User

class PublicacionForm(forms.ModelForm):
   # id_usuario = forms.CharField(required=False, disabled=True, widget=forms.TextInput(attrs= {'hidden': True}), label='')
   # id_mascota = forms.CharField(required=False, disabled=True, widget=forms.TextInput(attrs= {'hidden': True}), label='')
   # id_ubicacion = forms.CharField(required=False, disabled=True, widget=forms.TextInput(attrs= {'hidden': True}), label='')

   class Meta:
      model = Publicacion
      # fields = [
      #    'observaciones'
      # ]
      fields = [
         'observaciones',
      ]
      widgets = {
         'observaciones': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
      }

class MascotaForm(forms.ModelForm):
        
   id_dueño = forms.CharField(required=False, label='', widget=forms.TextInput(attrs= {'required':False, 'name': 'id_dueño', 'hidden': ''}))
   especie = forms.ChoiceField(choices=lista_especies)
   sexo = forms.ChoiceField(choices=Mascota.sexos)
   tamaño = forms.ChoiceField(choices=Mascota.tamanos)
   fotos = forms.ImageField(required=False)

   class Meta:
      model = Mascota
      exclude = [
      'id_dueño',
   ]
      # fields = '__all__'
      widgets = {
         # 'id_dueño': forms.TextInput(attrs= {'required':False, 'name': 'id_dueño'}),
         'nombre': forms.TextInput(attrs= {'class': 'form-control'}),
         'familia': forms.TextInput(attrs= {'class': 'form-control'}),
         'raza': forms.TextInput(attrs= {'class': 'form-control'}),
         'especie': forms.TextInput(attrs= {'class': 'form-control'}),
         'sexo': forms.TextInput(attrs= {'class': 'form-control'}),
         'color': forms.TextInput(attrs= {'class': 'form-control'}),
         'otro_dato': forms.Textarea(attrs= {'class': 'form-control', 'rows': 5, 'style': 'resize: none;'}),
         'edad': forms.TextInput(attrs= {'class': 'form-control'}),
         'tamaño': forms.TextInput(attrs= {'class': 'form-control'}),
         'fotos': forms.FileInput(attrs= {'class': 'form-control'}),
      }
      # labels = {
      #    'id_dueño': '',
      # }
      
class UbicacionForm(forms.ModelForm):
   localidad = forms.ChoiceField(choices=lista_localidades)
   
   class Meta:
      model = Ubicacion
      # exclude = [
      #    'id',
      # ]
      fields = '__all__'
      widgets = {
         'localidad': forms.TextInput(attrs= {'class': 'form-control'}),
         'barrio': forms.TextInput(attrs= {'class': 'form-control'}),
         'entre_calles': forms.TextInput(attrs= {'class': 'form-control'}),
         'numero': forms.TextInput(attrs= {'class': 'form-control'}),
         'calle': forms.TextInput(attrs= {'class': 'form-control'}),
         'otros_datos': forms.Textarea(attrs= {'class': 'form-control', 'rows': 2, 'style': 'resize: none;'}),
      }

class EncontroForm(forms.ModelForm):
   cuida = forms.ChoiceField(choices=Encontro.en_transito)
   fecha_limite = forms.DateField()
   
   class Meta:
      model = Encontro
      fields = [
         'cuida',
         'fecha_limite',
         ]
      widgets = {
         'cuida': forms.TextInput(attrs= {'class': 'form-control'}),
         'fecha_limite': forms.TextInput(attrs= {'class': 'form-control'}),
      }
      labels = {
         'cuida': 'Lo esta cuidando.?',
         'fecha_limite': 'Hasta cuando.?',
      }