from django.shortcuts import render
from main.models import Contacto
from main.forms import FormularioContacto
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
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
    return render(request, "consultas.html")

class ConsultasPerdidosView(generic.ListView):
    model=Perdido
    queryset=Perdido.objects.all()
    context_object_name = 'lista_perdidos'
    template_name='consultas_perdidos.html'

class ConsultasEncontradosView(generic.ListView):
    model=Encontro
    queryset=Encontro.objects.all()
    context_object_name = 'lista_encontrados'
    template_name='consultas_encontrados.html'