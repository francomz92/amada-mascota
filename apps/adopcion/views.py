from django.shortcuts import render
from .forms import *
from . import models
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import ListView,CreateView
# Create your views here.

def index(request):
    context = {}
    return render(request,'index.html',context)

class AdopcionList(ListView):
    model = Adopcion
    template_name = 'historial_adopciones.html'

class AdopcionCrear(CreateView):
    model = Adopcion
    template_name = 'crear_adopcion.html'
    form_class = AdopcionForm
    ubicacion_form_class = UbicacionForm
    mascota_form_class = MascotaForm
    succes_url = reverse_lazy('adopcion:historial_adopciones.html')

    def get_context_data(self,**kwargs):
        context = super(AdopcionCrear,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.ubicacion_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.mascota_form_class(self.request.GET)
        return context

    def post(self,request,*args,**kwargs):
        current_user = request.user
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.ubicacion_form_class(request.POST)
        form3 = self.mascota_form_class(request.POST, request.FILES,initial={'id_dueño': current_user})
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            adopcion = form.save(commit=False)
            adopcion.id_ubicacion = form2.save()
            adopcion.id_mascota = form3.save()
            adopcion.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            if not form.is_valid():
                return HttpResponse("fallo en Datos de adopcion")
            if not form2.is_valid():
                return HttpResponse("fallo ubicacion")
            if not form3.is_valid():
                return HttpResponse("fallo mascota")
            #return self.render_to_response(self.get_context_data(form = form,form2=form2,form3=form3))