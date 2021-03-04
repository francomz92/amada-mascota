from django.shortcuts import render
from main.models import Contacto
from main.forms import FormularioContacto
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView
from apps.perdidos.models import Perdido, Encontro

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




def consultas(request):
    ctx={
        'de_donde':"Consultar",
        'url_P': "consultas_perdidos",
        'url_E': "consultas_encontrados"
        }
    return render(request, "consultas.html",ctx)

class ConsultasPerdidosView(ListView):
    model=Perdido
    queryset=Perdido.objects.all()
    context_object_name = 'lista_perdidos'
    template_name='consultas_perdidos.html'

class ConsultasEncontradosView(ListView):
    model=Encontro
    queryset=Encontro.objects.all()
    context_object_name = 'lista_encontrados'
    template_name='consultas_encontrados.html'
