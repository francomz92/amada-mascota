from django import forms
from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields= ["nombre", "email", "asunto", "mensaje"]
        widgets = {
            'nombre': forms.TextInput(attrs={'type': 'text', 'class': 'form-control','name':'nombre','id':'nombre', 'placeholder': 'Tu nombre'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control','name':'email', 'id':'email', 'placeholder': 'Tu email'}),
            'asunto': forms.TextInput(attrs={'type': 'text', 'class': 'form-control','name':'asunto', 'id':'asunto', 'placeholder': 'Asunto'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control','name':'mensaje', 'rows':'5', 'placeholder': 'Tu mensaje'}), 
    }
