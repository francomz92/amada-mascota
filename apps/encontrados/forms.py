from django import forms
from .models import Publicacion


class PublicacionForm(forms.Form):
   
   class Meta:
      model = Publicacion
      fields = 'observaciones'

class MascotaForm(forms.Form):
   
   class Meta:
      model = Mascota
      fields = [
         'nombre',
         'familia',
         'raza',
         'edad',
         'sexo',
         'fotos',
         'color',
         'tamaño',
         'otros_datos',
      ]
      
class ubicacionForm(forms.Form):
   
   class Meta:
      model = Ubicacion
      fields = [
         'localidad',
         'barrio',
         'entre_calles',
         'numero',
         'calle',
         'otros_datos',
      ]
