from django import forms
from .models import Publicacion, Mascota, Ubicacion


class PublicacionForm(forms.Form):
   
   class Meta:
      model = Publicacion
      fields = 'observaciones'

class MascotaForm(forms.Form):
   
   class Meta:
      model = Mascota
      exclude = [
         'id_mascota',
         'id_usuario',
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
      #    'otros_datos',
      # ]
      
class UbicacionForm(forms.Form):
   
   class Meta:
      model = Ubicacion
      exclude = [
         'id_ubicacion',
      ]
      # fields = [
      #    'localidad',
      #    'barrio',
      #    'entre_calles',
      #    'numero',
      #    'calle',
      #    'otros_datos',
      # ]