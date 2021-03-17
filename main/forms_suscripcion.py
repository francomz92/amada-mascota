from django import forms
from apps.perdidos.models import Notificacion, Publicacion, Mascota, Ubicacion, Encontro, lista_especies, lista_localidades
from django.contrib.auth.models import User


class SusPerdidoForm(forms.ModelForm):
   
    class Meta:
        model = Notificacion
        exclude = [
            'id_usuario'
        ]

        widgets = {
            'tipo': forms.Select(choices= Notificacion.tipo_notificacion, attrs= {'class': 'form-control', 'name': 'tipo'}),
            'especie': forms.Select(choices= lista_especies, attrs= {'class': 'form-control', 'name': 'especie'}),
            'localidad':forms.Select(choices= lista_localidades, attrs= {'class': 'form-control', 'name': 'localidad'}),
            'fecha_hasta': forms.DateInput(attrs= {'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}), 
        }
      
        labels = {
            'fecha_hasta': '¿Hasta cuándo?',
        }
        help_texts = {
            'fecha_hasta': '¿Hasta qué fecha desea recibir las notificaciones?',
        }

