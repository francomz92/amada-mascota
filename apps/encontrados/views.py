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
   # publicacion = PublicacionForm()
   mascota = MascotaForm(initial= {'id_dueño': current_user})
   ubicacion = UbicacionForm()
   encontro = EncontroForm(initial= {'id_usuario': current_user})
   if request.method == 'POST':
      mascota = MascotaForm(data=request.POST, files=request.FILES)
      # mascota.id_dueño = User.objects.filter(username=current_user)
      ubicacion = UbicacionForm(data=request.POST)
      # publicacion = PublicacionForm(data=request.POST)
      encontro = EncontroForm(data=request.POST)
      # encontro.id_usuario = User.objects.filter(username=current_user)
      # publicacion.id_usuario = User.objects.filter(username=current_user)
      # publicacion.id_mascota = Mascota.objects.filter(otro_dato=request.POST['otro_dato']).filter(id_dueño=current_user)
      # publicacion.id_ubicacion = Ubicacion.objects.filter(localidad=request.POST['localidad']).filter(barrio=request.POST['barrio']).filter(entre_calles=request.POST['entre_calles']).filter(calle=request.POST['calle']).filter(otros_datos=request.POST['otros_datos'])
      if mascota.is_valid():
         mascota.save()
         if ubicacion.is_valid():
            ubicacion.save()
         # encontro = EncontroForm(data=request.POST, initial= {'id_macota': Mascota.objects.filter(id_dueño=current_user).filter(otro_dato=mascota.cleaned_data('otro_dato')), 'id_ubicacion': Ubicacion.objects.filter(localidad=ubicacion.cleaned_data('localidad')).filter(barrio=ubicacion.cleaned_data('barrio')).filter(entre_calles=ubicacion.cleaned_data('entre_calles')).filter(calle=ubicacion.cleaned_data('calle')).filter(otros_datos=ubicacion.cleaned_data('otros_datos'))})
         # encontro.id_usuario = current_user
         # encontro.id_mascota = Mascota.objects.filter(otro_dato=request.POST['otro_dato']).filter(id_dueño=encontro.id_usuario)
         # encontro.id_ubicacion = Ubicacion.objects.filter(localidad=request.POST['localidad']).filter(barrio=request.POST['barrio']).filter(entre_calles=request.POST['entre_calles']).filter(calle=request.POST['calle']).filter(otros_datos=request.POST['otros_datos'])
            if encontro.is_valid():
               # publicacion.save(commit=False)
               encontro.save()
               vigencia = encontro.cleaned_data['fecha_limite']
               messages.success(request, message=f'Su publicación ha sido un exito.!! Recuerda renovarla antes del {vigencia}')
               return redirect(to='encontrados:lista_encontrados')
            else:
               messages.error(request, message='Ups...parece que algo salió mal.!! Vuelve a intentarlo.')
               mascota = MascotaForm(data=request.POST, files=request.FILES)
               ubicacion = UbicacionForm(data=request.POST)
               # publicacion = PublicacionForm(data=request.POST)
               encontro = EncontroForm(data=request.POST)
   
   ctx = {
      'mascota': mascota,
      'ubicacion': ubicacion,
      # 'publicacion': publicacion,
      'encontro': encontro,
      }
   return render(request, 'publicar.html', ctx)

@login_required
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

def buscar(request):
   if request.GET['buscar']:
      mascota = request.GET['buscar']
      if mascota is not None:
         resultado = Mascota.objects.filter(nombre=mascota) # Revisar
         ctx = {
            'resultado': resultado,
            'busqueda': mascota,
         }
         if resultado:
            return render('resultado_busqueda.html', ctx)
         else:
            messages.info(request, message=f'No se encontro {mascota}')
      else:
         return redirect(to='encontrados:lista_encontrados')
   return render(request, 'lista_encontrados.html')