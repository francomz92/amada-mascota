from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms

# Create your views here.
class AgregarPublicacion(CreateView):
	model = models.Publicacion
	form_class = forms.FormularioPublicacion
	template_name = 'agregar_publicacion.html'
	#fields = '__all__'