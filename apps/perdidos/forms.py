from django import forms
from .models import Perdido
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta


class PerdidoForm(forms.ModelForm):

   gratificacion = forms.CharField(max_length=150,
                                   error_messages={'max_length': '¡Máximo permitido 150 caracteres!'})

   class Meta:
      model = Perdido
      exclude = [
          'id_usuario',
          'id_mascota',
          'id_ubicacion',
          'valido_hasta',
          'fecha_entrega',
      ]
      widgets = {
          'fecha_perdido':
          forms.DateInput(
              attrs={
                  'type': 'date',
                  'max': now().date(),
                  'min': now().date() + relativedelta(years=-20),
              },
              format='%Y-%m-%d',
          ),
          'edad':
          forms.TextInput(attrs={
              'maxlength': 2,
              'pettern': '\d*',
          }),
      }
