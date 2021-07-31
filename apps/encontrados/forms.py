from dateutil.relativedelta import relativedelta
from django import forms
from django.utils.timezone import now
from .models import Encontro


class EncontradoForms(forms.ModelForm):
   class Meta:
      model = Encontro
      exclude = [
          'id_usuario',
          'id_mascota',
          'id_ubicacion',
          'fecha_entrega',
          'valido_hasta',
      ]
      widgets = {
          'fecha_encontrado':
          forms.DateInput(
              attrs={
                  'type': 'date',
                  'max': now().date(),
                  'min': now().date() + relativedelta(years=-20),
              },
              format='%Y-%m-%d',
          ),
      }
