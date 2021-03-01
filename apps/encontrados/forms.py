from django import forms
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro, lista_especies, lista_localidades
from django.contrib.auth.models import User

class PublicacionForm(forms.ModelForm):
   # id_usuario = forms.CharField(widget=forms.TextInput(attrs={'name': 'id_usuario'}), disabled=True, required=False)
   # id_mascota = forms.CharField(widget=forms.TextInput(attrs={'name': 'id_mascota'}), disabled=True, required=False)
   # id_ubicacion = forms.CharField(widget=forms.TextInput(attrs={'name': 'id_ubicacion'}), disabled=True, required=False)

   class Meta:
      model = Publicacion
      # fields = [
      #    'observaciones'
      # ]
      # fields = '__all__'
      exclude = {
         'id_usuario',
         'id_mascota',
         'id_ubicacion',
      }
      widgets = {
         'observaciones': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
      }
      
class MascotaForm(forms.ModelForm):
        
   # id_dueño = forms.ChoiceField(choices= User, required=False, label='asdas')
   # especie = forms.ChoiceField(choices=lista_especies)
   # sexo = forms.ChoiceField(choices=Mascota.sexos)
   # tamaño = forms.ChoiceField(choices=Mascota.tamanos)
   # fotos = forms.ImageField(required=False)

   class Meta:
      model = Mascota
   #    exclude = [
   #    'id_dueño',
   # ]
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
         'edad': forms.TextInput(attrs= {'class': 'form-control'}),
         'tamaño': forms.Select(attrs= {'class': 'form-control'}),
         'fotos': forms.FileInput(attrs= {'class': 'form-control'}),
      }
      labels = {
         'id_dueño': '',
      }
class UbicacionForm(forms.ModelForm):
   localidad = forms.ChoiceField(choices=lista_localidades)
   
   class Meta:
      model = Ubicacion
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
   # cuida = forms.ChoiceField(choices=Encontro.en_transito, label='Los esta cuidando.? ')
   # fecha_limite = forms.DateField(widget=forms.TextInput(attrs= {'name': 'fecha_limite'}), label='Hasta cuando.? ')
   # id_usuario = forms.CharField(required=False, label='', widget=forms.Select(attrs= {'required':False, 'name': 'id_usuario'}))
   # id_mascota = forms.CharField(required=False, label='', widget=forms.Select(attrs= {'required':False, 'name': 'id_mascota'}))
   # id_ubicacion = forms.CharField(required=False, label='', widget=forms.Select(attrs= {'required':False, 'name': 'id_ubicacion'}))
   # fecha_evento = forms.CharField(required=False, label='', widget=forms.TextInput(attrs= {'required':False, 'name': 'fecha_evento', 'hidden': ''}))
   # fecha_entrega = forms.CharField(required=False, label='', widget=forms.TextInput(attrs= {'required':False, 'name': 'fecha_entrega', 'hidden': ''}))
   # id_usuario = forms.CharField(widget=forms.TextInput(attrs={'name': 'id_usuario'}), disabled=True, required=False)
   # id_mascota = forms.CharField(widget=forms.TextInput(attrs={'name': 'id_mascota'}), disabled=True, required=False)
   # id_ubicacion = forms.CharField(widget=forms.TextInput(attrs={'name': 'id_ubicacion'}), disabled=True, required=False)
   
   class Meta:
      model = Encontro
      # fields = [
      #    'cuida',
      #    'fecha_limite',
      #    ]
      # fields = '__all__'
      exclude = [
         'id_usuario',
         'id_mascota',
         'id_ubicacion',
         'fecha_evento',
         'fecha_entrega',
      ]
      widgets = {
         'cuida': forms.Select(choices= Encontro.en_transito, attrs= {'class': 'form-control', 'name': 'cuida'}),
         'fecha_limite': forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'mm/dd/aaaa'}),
         'observaciones': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
         # 'id_usuario': forms.Select(attrs= {'required':None, 'name': 'id_usuario', 'hidden': '',}),
         # 'id_mascota': forms.Select(attrs= {'required':None, 'name': 'id_mascota', 'hidden': '',}),
         # 'id_ubicacion': forms.Select(attrs= {'required':False, 'name': 'id_ubicacion', 'hidden': '',}),
      }
      labels = {
         'cuida': 'Lo esta cuidando.?',
         'fecha_limite': 'Hasta cuando.?',
      }
      help_texts = {
         'fecha_limite': 'En caso de cuidarlo indique hasta cuando',
      }