from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView
# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html',context)

class AdopcionList(ListView):
    model = Adopcion
    template = 'adopcion:index.html'

class AdopcionCrear(CreateView):
    model = Adopcion
    template = 'adopcion:adopciones_listar'
    form_class = AdopcionForm
    ubicacion_form_class = UbicacionForm
    mascota_form_class = MascotaForm
    succes_url = reverse_lazy('adopcion:adopciones_listar')

    def get_context_data(self,**kwargs):
        context = super(AdopcionCrear,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form' not in context:
            context['form2'] = self.ubicacion_form_class(self.request.GET)
        if 'form' not in context:
            context['form3'] = self.mascota_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.ubicacion_form_class(request.POST)
        form3 = self.mascota_form_class(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            adopcion = form.save(commit=False)
            adopcion.id_ubicacion = form2.save()
            adopcion.id_mascota = form3.save()
            adopcion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form,form2=form2,form3=form3))