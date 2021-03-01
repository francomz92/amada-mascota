from django.shortcuts import render
from main.models import Contacto
from main.forms import FormularioContacto
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic
from apps.perdidos.models import Perdido

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




def busquedas(request):
    return render(request, "busquedas.html")

class BusquedasPerdidosView(generic.ListView):
    model=Perdido
    queryset=Perdido.objects.all()
    context_object_name = 'lista_perdidos'
    template_name='busquedas_perdidos.html'