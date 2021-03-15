from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegistroUsuario(generic.CreateView):
    form_class = forms.FormularioRegistro
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class LoginUsuario(auth_views.LoginView):
    form_class = forms.LoginForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

@login_required
def perfil(request):
    current_user = request.user.id
    perfil = get_object_or_404(User, id=current_user)
    ctx = {
        'perfil':perfil
    }
    return render(request,'mi_perfil/mis_datos.html', ctx)

@login_required
def perfilActualizar(request):
    perfil = get_object_or_404(User, id=request.user.id)
    if request.method=="GET":
        form = forms.Actualizar(instance=request.user)
    else:
        form = forms.Actualizar(data=request.POST,instance = request.user)
        if form.is_valid():
            """form.user_name = request.POST['user_name']
            form.first_name = request.POST['first_name']
            form.last_name = request.POST['last_name']
            form.email = request.POST['email']"""
            form.save()
        return redirect('perfil')
    return render(request, "mi_perfil/editar_datos.html", {'form':form}) 