from django import forms
from .models import Adopcion


class AdopcionForms(forms.ModelForm):

   condicion = forms.CharField(required=True,
                               max_length=800,
                               error_messages={'max_length': '¡Máximo permitido 800 caracteres!'})

   class Meta:
      model = Adopcion
      exclude = [
          'id_usuario',
          'id_mascota',
          'id_ubicacion',
          'fecha_entrega',
          'valido_hasta',
      ]
