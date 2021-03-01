from django.shortcuts import render, redirect, get_object_or_404
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Encontro
from .forms import PublicacionForm, MascotaForm, UbicacionForm, EncontroForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def lista_encontrados(request):
   publicaciones = Encontro.objects.all()
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
   # current_user = request.user
   encontro = get_object_or_404(Encontro, id=id_publicacion)
   # publicacion = get_object_or_404(Publicacion, id=id_publicacion)
   mascota = get_object_or_404(Mascota, id=encontro.id_mascota.id)
   ubicacion = get_object_or_404(Ubicacion, id=encontro.id_ubicacion.id)
   ctx = {
      # 'publicacion': PublicacionForm(instance=publicacion),
      'mascota': MascotaForm(instance=mascota),
      'ubicacion': UbicacionForm(instance=ubicacion),
      'encontro': EncontroForm(instance=encontro),
   }
   if request.method == 'GET':
      # publicacion = PublicacionForm(data=request.GET, instance=publicacion)
      mascota = MascotaForm(data=request.GET, files=request.GET, instance=mascota)
      ubicacion = UbicacionForm(data=request.GET, instance=ubicacion)
      encontro = EncontroForm(data=request.GET, instance=encontro)
      if mascota.is_valid() and ubicacion.is_valid() and encontro.is_valid():
         # publicacion.save()
         mascota.save()
         ubicacion.save()
         encontro.save()
         messages.success(request, message='Guardado')
         return redirect(to='encontrados:lista_encontrados')
      else:
         messages.error(request, message='Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
   # ctx = {
   #    # 'publicacion': PublicacionForm(instance=publicacion),
   #    'mascota': MascotaForm(instance=mascota),
   #    'ubicacion': UbicacionForm(instance=ubicacion),
   #    'encontro': EncontroForm(instance=encontro),
   # }
   return render(request, 'editar_publicacion.html', ctx)

def buscar(request):
   if request.GET['buscar']:
      mascota = request.GET['buscar']
      if mascota is not None:
         firs = Mascota.objects.filter(raza=mascota)
         resultado = Publicacion.objects.filter(id_mascota=firs) # Revisar
         ctx = {
            'resultado': resultado,
            'busqueda': mascota,
         }
         return render(request, 'resultado_busqueda.html', ctx)
         # if resultado:
         # else:
         #    messages.info(request, message=f'No se encontro {mascota}')
      else:
         return redirect(to='encontrados:lista_encontrados')
   return render(request, 'lista_encontrados.html')