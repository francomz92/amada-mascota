from django import forms
from django.forms.models import ALL_FIELDS
from .models import LISTA_ESPECIES, LISTA_LOCALIDADES, Mascota, Ubicacion


class SearchPerdidosEncontraodsForm(forms.Form):
   especie = forms.ChoiceField(choices=LISTA_ESPECIES, required=False)
   localidad = forms.ChoiceField(choices=LISTA_LOCALIDADES, required=False)
   barrio = forms.CharField(max_length=50, strip=True, required=False)


class MascotaForm(forms.ModelForm):
   class Meta:
      model = Mascota
      fields = ALL_FIELDS

class UbicacionForm(forms.ModelForm):
   class Meta:
      model = Ubicacion
      fields = ALL_FIELDS
