from django import forms
from apps.perdidos.models import Ubicacion,Mascota,Adopcion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields =  '__all__'

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fileds = '__all__'
        exclude = ['id_dueño']

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'
        exclude =  ['id_usuario','id_mascota','id_ubicacion']