from django.shortcuts import render
from main.models import Contacto
from main.forms import FormularioContacto
from django.http import HttpResponse, HttpResponseRedirect

#magui para consultas y para suscripciones
from django.views.generic import ListView , UpdateView ## para vistas x class dsps borrar Magui
from apps.perdidos.models import Notificacion, Publicacion, Mascota, Ubicacion, Perdido, Encontro, lista_especies, lista_localidades
from .forms_suscripcion import SusPerdidoForm
from django.contrib import messages
from datetime import datetime, date, time, timedelta
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about(request):
    if request.method == 'POST':
        form = FormularioContacto(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
    else:
        form = FormularioContacto()
        context = {
            'form':form,
        }
    return render(request, 'about.html', {'form':form})



def suscripciones(request):
   current_user = request.user
   
   suscrip = SusPerdidoForm(initial= {'id_dueño': current_user})
   
   if request.method == 'POST':
      
      suscrip = SusPerdidoForm(data=request.POST, files=request.FILES)
      
      if suscrip.is_valid():
         suscripto = suscrip.save(commit=False)
         suscripto.id_usuario= current_user
         suscripto.save()
         messages.success(request, message='Suscripcion Correcta!!')
         return redirect(to='suscripciones')
      else:
         messages.error(request, message='Error. Vuelva a cargar los datos.')
         suscrip = SusPerdidoForm(data=request.POST, files=request.FILES)
         
   ctx = {
      'suscrip_per': suscrip,
      }
   return render(request, 'suscripcion_publicaciones.html', ctx)


def suscripciones_ver(request):
    usuario_login=request.user.id
    lista= Notificacion.objects.filter(id_usuario__id=usuario_login).exclude(fecha_hasta__lt = datetime.now())
    lista=lista.order_by("fecha_desde")[:12]
    ctx = {
        'lista_suscripciones': lista,
      }
    return render(request, 'suscripcion_publicacionVer.html', ctx) 