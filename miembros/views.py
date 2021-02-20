from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import views as auth_views

# Create your views here.

class RegistroUsuario(generic.CreateView):
    form_class = forms.FormularioRegistro
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class LoginUsuario(auth_views.LoginView):
    form_class = forms.LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')