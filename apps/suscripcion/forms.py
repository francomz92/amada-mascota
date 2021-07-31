from django import forms
from .models import Suscripcion


class PrivateSuscripcionesForm(forms.ModelForm):
   class Meta:
      model = Suscripcion
      fields = ['suscripcion']
