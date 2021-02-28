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

# @login_required
def publicar(request):
   current_user = request.user
   # publicacion = PublicacionForm(initial={'id_usuario': current_user})
   mascota = MascotaForm(initial= {'id_dueño': current_user})
   ubicacion = UbicacionForm()
   encontro = EncontroForm(initial= {'id_usuario': current_user})
   if request.method == 'POST':
      mascota = MascotaForm(data=request.POST, files=request.FILES)
      # mascota.id_dueño = User.objects.filter(username=current_user)
      ubicacion = UbicacionForm(data=request.POST)
      # publicacion = PublicacionForm(data=request.POST)
      encontro = EncontroForm(data=request.POST, initial={'id_usuario': current_user})
      # encontro.id_usuario = User.objects.filter(username=current_user)
      # publicacion.id_usuario = User.objects.filter(username=current_user)
      # publicacion.id_mascota = Mascota.objects.filter(otro_dato=request.POST['otro_dato']).filter(id_dueño=current_user)
      # publicacion.id_ubicacion = Ubicacion.objects.filter(localidad=request.POST['localidad']).filter(barrio=request.POST['barrio']).filter(entre_calles=request.POST['entre_calles']).filter(calle=request.POST['calle']).filter(otros_datos=request.POST['otros_datos'])
      if mascota.is_valid():
         masc = mascota.save()
         # masc.id_dueño = User.objects.filter(username=current_user)
         # masc.save()
         if ubicacion.is_valid():
            ubic = ubicacion.save()
            # pub = publicacion.save(commit=False)
            # pub.id_usuario = current_user
            # pub.id_mascota = masc
            # pub.id_ubicacion = ubic
            enc = encontro.save(commit=False)
            enc.id_usuario = current_user
            enc.id_mascota = masc
            enc.id_ubicacion = ubic
            # publicacion.save(commit=False)
            # publicacion.id_usuario = current_user
            # publicacion.id_mascota = masc
            # publicacion.id_ubicacion = ubic
            # encontro.save(commit=False)
            # encontro.id_usuario = current_user
            # encontro.id_mascota = masc
            # encontro.id_ubicacion = ubic
            if encontro.is_valid():
               # publicacion.save()
               # encontro.save()
               # pub.save()
               enc.save()
      # if encontro.is_valid() and publicacion.is_valid() and mascota.is_valid() and ubicacion.is_valid():
      #    ubic = ubicacion.save()
      #    masc = mascota.save(commit=False)
      #    masc.id_dueño = current_user
      #    masc.save()
      #    pub = publicacion.save(commit=False)
      #    pub.id_usuario = current_user
      #    pub.id_mascota = masc
      #    pub.id_ubicacion = ubic
      #    pub.save()
      #    enc = encontro.save(commit=False)
      #    enc.id_usuario = current_user
      #    enc.id_mascota = masc
      #    enc.id_ubicacion = ubic
      #    enc.save()
         # publicacion.save(commit=False)
         # encontro.save(commit=False)
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

# @login_required
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