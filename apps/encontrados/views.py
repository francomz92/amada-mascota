from django.shortcuts import render, redirect, get_object_or_404
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro
from .forms import MascotaForm, UbicacionForm, EncontroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def lista_encontrados(request):
   current_user = request.user
   publicaciones = Encontro.objects.filter(id_usuario=current_user)
   ctx = {
      'publicaciones': publicaciones,
   }
   return render(request, 'lista_encontrados.html', ctx)

@login_required
def publicar(request):
   current_user = request.user
   mascota = MascotaForm(initial= {'id_dueño': current_user})
   ubicacion = UbicacionForm()
   encontro = EncontroForm(initial= {'id_usuario': current_user})
   if request.method == 'POST':
      mascota = MascotaForm(data=request.POST, files=request.FILES)
      ubicacion = UbicacionForm(data=request.POST)
      encontro = EncontroForm(data=request.POST, initial={'id_usuario': current_user})
      if mascota.is_valid():
         masc = mascota.save()
         if ubicacion.is_valid():
            ubic = ubicacion.save()
            enc = encontro.save(commit=False)
            enc.id_usuario = current_user
            enc.id_mascota = masc
            enc.id_ubicacion = ubic
            if encontro.is_valid():
               enc.save()
               vigencia = encontro.cleaned_data['fecha_limite']
               messages.success(request, message=f'Su publicación ha sido un exito.!! Recuerda renovarla antes del {vigencia}')
               return redirect(to='encontrados:lista_encontrados')
      else:
         messages.error(request, message='Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
         mascota = MascotaForm(data=request.POST, files=request.FILES)
         ubicacion = UbicacionForm(data=request.POST)
         encontro = EncontroForm(data=request.POST)
   
   ctx = {
      'mascota': mascota,
      'ubicacion': ubicacion,
      'encontro': encontro,
      }
   return render(request, 'publicar.html', ctx)

@login_required
def editar_publicacion(request, id_publicacion):
   encontro = get_object_or_404(Encontro, id=id_publicacion)
   mascota = get_object_or_404(Mascota, id=encontro.id_mascota.id)
   ubicacion = get_object_or_404(Ubicacion, id=encontro.id_ubicacion.id)
   ctx = {
      'mascota': MascotaForm(instance=mascota),
      'ubicacion': UbicacionForm(instance=ubicacion),
      'encontro': EncontroForm(instance=encontro),
   }
   if request.method == 'POST':
      mascota = MascotaForm(data=request.POST, files=request.POST, instance=mascota)
      ubicacion = UbicacionForm(data=request.POST, instance=ubicacion)
      encontro = EncontroForm(data=request.POST, instance=encontro)
      if mascota.is_valid() and ubicacion.is_valid() and encontro.is_valid():
         mascota.save()
         ubicacion.save()
         encontro.save()
         messages.success(request, message='Guardado')
         return redirect(to='encontrados:lista_encontrados')
      else:
         messages.error(request, message='Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
   return render(request, 'editar_publicacion.html', ctx)

@login_required
def publicacion(request, id_publicacion):
   publicacion = get_object_or_404(Encontro, id=id_publicacion)
   ctx = {
      'publicacion': publicacion,
   }
   return render(request, 'publicacion.html', ctx)