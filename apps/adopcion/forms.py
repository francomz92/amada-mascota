from django import forms
from apps.perdidos.models import Ubicacion,Mascota,Adopcion

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields =  '__all__'
        widgets = {
         'localidad': forms.Select(attrs= {'class': 'form-control'}),
         'barrio': forms.TextInput(attrs= {'class': 'form-control'}),
         'entre_calles': forms.TextInput(attrs= {'class': 'form-control'}),
         'numero': forms.TextInput(attrs= {'class': 'form-control'}),
         'calle': forms.TextInput(attrs= {'class': 'form-control'}),
         'otros_datos': forms.Textarea(attrs= {'class': 'form-control', 'rows': 2, 'style': 'resize: none;'}),
        }
        labels = {
            'otros_datos': 'Alguna referencia',
        }
        

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fileds = '__all__'
        exclude = ['id_dueño']
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
            'nombre': 'Mascota',
            'otro_dato': 'Alguna descripción adicional',
            'edad': 'Edad aproximada',
        }

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'
        exclude =  ['id_usuario','id_mascota','id_ubicacion','fecha_entrega','fecha_publicacion']
        widgets = {
            'condicion':forms.Textarea(attrs= {'class': 'form-control', 'rows': 3, 'style': 'resize: none;'}),
        }