from django.shortcuts import render, redirect, get_object_or_404
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro
from .forms import PublicacionForm, MascotaForm, UbicacionForm, EncontroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def lista_encontrados(request):
   publicaciones = Publicacion.objects.all()
   ctx = {
      'publicaciones': publicaciones,
   }
   return render(request, 'lista_encontrados.html', ctx)

# @login_required
def publicar(request):
   publicacion = PublicacionForm()
   mascota = MascotaForm()
   ubicacion = UbicacionForm()
   encontro = EncontroForm()
   if request.method == 'GET':
      publicacion = PublicacionForm(data=request.GET)
      mascota = MascotaForm(data=request.GET, files=request.FILES)
      ubicacion = UbicacionForm(data=request.GET)
      encontro = EncontroForm(data=request.GET)
      if publicacion.is_valid() and mascota.is_valid() and ubicacion.is_valid() and encontro.is_valid():
         publicacion.save()
         mascota.save()
         ubicacion.save()
         encontro.save()
         vigencia = encontro.cleaned_data['fecha_limite']
         messages.success(request, message=f'Su publicación ha sido un exito.!! Recuerda renovarla antes del {vigencia}')
         return redirect(to='encontrados:lista_encontrados')
      else:
         messages.error(request, message='Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
         publicacion = PublicacionForm(data=request.GET)
         mascota = MascotaForm(data=request.GET, files=request.FILES)
         ubicacion = UbicacionForm(data=request.GET)
         encontro = EncontroForm(data=request.GET)
   ctx = {
      'publicacion': publicacion,
      'mascota': mascota,
      'ubicacion': ubicacion,
      }
   return render(request, 'publicar.html', ctx)

# @login_required
def editar_publicacion(request, id_publicacion):
   current_user = request.user
   publicacion = get_object_or_404(Publicacion, id=id_publicacion, id_usuario=current_user)
   mascota = get_object_or_404(Mascota, id=publicacion.id_mascota.id)
   ubicacion = get_object_or_404(Ubicacion, id=publicacion.id_ubicacion.id)
   encontro = get_object_or_404(Encontro, id_publicacion=id_publicacion)
   ctx = {
      'publicacion': PublicacionForm(instance=publicacion),
      'mascota': MascotaForm(instance=mascota),
      'ubicacion': UbicacionForm(instance=ubicacion),
      'encontro': EncontroForm(instance=encontro),
   }
   if request.method == 'GET':
      publicacion = PublicacionForm(data=request.GET, instance=publicacion)
      mascota = MascotaForm(data=request.GET, files=request.GET, instance=mascota)
      ubicacion = UbicacionForm(data=request.GET, instance=ubicacion)
      encontro = EncontroForm(data=request.GET, instance=encontro)
      if publicacion.is_valid() and mascota.is_valid() and ubicacion.is_valid() and encontro.is_valid():
         publicacion.save()
         mascota.save()
         ubicacion.save()
         encontro.save()
         messages.success(request, message='Guardado')
         return redirect(to='encontrados:lista_encontrados')
      else:
         messages.error(request, message='Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
   ctx = {
      'publicacion': PublicacionForm(instance=publicacion),
      'mascota': MascotaForm(instance=mascota),
      'ubicacion': UbicacionForm(instance=ubicacion),
      'encontro': EncontroForm(instance=encontro),
   }
   return render(request, 'editar_publicacion.html', ctx)


"""from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms

# Create your views here.
class AgregarPublicacion(CreateView):
	model = models.Publicacion
	form_class = forms.FormularioPublicacion
	template_name = 'agregar_publicacion.html'
	#fields = '__all__'"""