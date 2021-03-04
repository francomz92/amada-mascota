from django.shortcuts import render
from main.models import Contacto
from main.forms import FormularioContacto
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView ## para vistas x class dsps borrar Magui
from apps.perdidos.models import Publicacion, Mascota, Ubicacion, Perdido, Encontro, lista_especies, lista_localidades

from .forms_consultas import FomularioConsultas
from datetime import datetime, date, time, timedelta

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



def consultas_perdidos(request):
    if request.method=="POST":
        miFormulario= FomularioConsultas(request.POST)
        if miFormulario.is_valid():
            
            info_forms=miFormulario.cleaned_data
        
            espe = str(info_forms['especie_choice'])
            #loca = str(info_forms['localidad_choice'])
            
            lista_perdidos=Perdido.objects.filter(id_mascota__especie__icontains=espe)
        
    else:
        lista_perdidos=Perdido.objects.all()
        miFormulario=FomularioConsultas()
    
    lista_perdidos=lista_perdidos.exclude(fecha_entrega__isnull=False).order_by("fecha_evento").reverse()[:10]
    ctx={
        "form": miFormulario,
        "lista_perdidos":lista_perdidos,
        }
    return render(request, "consultas_perdidos.html", ctx)


class ConsultasEncontradosView(ListView):
    model=Encontro
    queryset=Encontro.objects.all()
    context_object_name = 'lista_encontrados'
    template_name='consultas_encontrados.html'