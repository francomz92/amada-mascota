from django import forms
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro, lista_especies, lista_localidades
from django.contrib.auth.models import User

class  FomularioConsultas(forms.Form):
    #asunto=forms.CharField( label="Asunto" , max_length = 50) #initial="el asunto",
    especie_choice= forms.ChoiceField(
        label="Especie:",
        choices=lista_especies,
        #help_text="Selecciona la especie"
        )
    localidad_choice= forms.ChoiceField(
        label="Localidad:", 
        choices=lista_localidades
        )
    sexo_choice= forms.ChoiceField(
        label="Sexo:", 
        choices=Mascota.sexos
        )
    """ barrio=forms.CharField( 
        label="Barrio:", 
        max_length = 50) #initial="aqui escriba el barrio", """