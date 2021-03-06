from django.shortcuts import render,redirect
from .forms import *
from . import models
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime, timedelta
from django.utils import timezone
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

def index(request):
    context = {}
    return render(request,'index.html',context)    

class misAdopciones(ListView):
    model = Adopcion
    template_name = 'historial_adopciones.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(id_usuario=self.request.user)

class AdopcionCrear(CreateView):
    model = Adopcion
    template_name = 'crear_adopcion.html'
    form_class = AdopcionForm
    ubicacion_form_class = UbicacionForm
    mascota_form_class = MascotaForm
    success_url = reverse_lazy('adopcion:adopciones_listar')

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
        form = self.form_class(request.POST,initial={'id_usuario': current_user})
        form2 = self.ubicacion_form_class(request.POST)
        form3 = self.mascota_form_class(request.POST, request.FILES,initial={'id_usuario_id': current_user})
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            adopcion = form.save(commit=False)
            adopcion.id_usuario = current_user
            adopcion.id_ubicacion = form2.save()
            adopcion.id_mascota = form3.save()
            adopcion.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form,form2=form2,form3=form3))

class AdopcionRenovar(UpdateView):
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'adopcion_renovar.html'
    success_url = reverse_lazy('adopcion:adopciones_listar')

    def get_context_data(self,**kwargs):
        context = super(AdopcionRenovar,self).get_context_data(**kwargs)
        return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST,instance = self.get_object())
        if  form.is_valid():
            adopcion = form.save(commit=False)
            adopcion.valido_hasta = timezone.now() + timezone.timedelta(days=7)
            adopcion.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("fallo")

class AdopcionActualizar(UpdateView):
    model = Adopcion
    form_class = AdopcionForm
    ubicacion_form_class = UbicacionForm
    mascota_form_class = MascotaForm
    template_name = 'crear_adopcion.html'
    success_url = reverse_lazy('adopcion:adopciones_listar')
    
    def get_context_data(self,**kwargs):
        context = super(AdopcionActualizar,self).get_context_data(**kwargs)
        if 'form2' not in context:
            context['form2'] = self.ubicacion_form_class(instance = self.object.id_ubicacion)
        if 'form3' not in context:
            context['form3'] = self.mascota_form_class(instance = self.object.id_mascota)
        return context

    def post(self,request,*args,**kwargs):
        current_user = request.user
        self.object = self.get_object
        form = self.form_class(request.POST,initial={'id_usuario': current_user},instance = self.get_object())
        form2 = self.ubicacion_form_class(request.POST,instance = self.get_object().id_ubicacion)
        form3 = self.mascota_form_class(request.POST,request.FILES,initial={'id_usuario_id': current_user},instance = self.get_object().id_mascota)
        if form.is_valid() and form2.is_valid() and form3.is_valid():
            adopcion = form.save(commit=False)
            adopcion.id_usuario = current_user
            adopcion.id_ubicacion = form2.save()
            adopcion.id_mascota = form3.save()
            adopcion.save()
            form3.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form = form,form2=form2,form3=form3))

class AdopcionEliminar(DeleteView):
    model = Adopcion
    form_class = AdopcionForm
    template_name = 'adopcion_eliminar.html'
    success_url = reverse_lazy('adopcion:adopciones_listar')
    
