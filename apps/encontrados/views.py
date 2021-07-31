from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from utils.decorators import contex_data
from apps.models import Mascota, Ubicacion
from apps.forms import SearchPerdidosEncontraodsForm, MascotaForm, UbicacionForm
from .models import Encontro
from .forms import EncontradoForms

# Create your views here.


@method_decorator(contex_data(title='Encontrados', header='Consulta Encontrados'), name='get_context_data')
class PublicEncontrados(ListView):
   model = Encontro
   template_name = 'public_encontrados.html'
   form_class = SearchPerdidosEncontraodsForm

   def get(self, request, *args, **kwargs):
      form = SearchPerdidosEncontraodsForm(request.GET)
      if form.is_valid():
         result = self.model.objects.all().filter(
             id_mascota__especie__icontains=request.GET.get('especie', ''),
             id_ubicacion__localidad__icontains=request.GET.get('localidad', ''),
             id_ubicacion__barrio__icontains=request.GET.get('barrio', ''),
         ).order_by('fecha_publicacion')
         data = self.get_context_data()
         data['form'] = form
         data['publicaciones'] = result
         return render(request, self.template_name, data)
      return super().get(request, *args, **kwargs)

   def get_context_data(self, **kwargs):
      data = {
          'form': self.form_class(),
          'msj': 'Estas mascotas se encuentran sin dueño.',
      }
      return data


@method_decorator(login_required(), name='dispatch')
@method_decorator(contex_data(title='Mis Publicaciones', header='Encontrados'), name='get_context_data')
class PrivateEncontrados(ListView):
   model = Encontro
   template_name = 'private_encontrados.html'
   context_object_name = 'publicaciones'

   def get_queryset(self):
      self.object = self.model.objects.filter(id_usuario=self.request.user)\
                                      .order_by('fecha_publicacion')
      return self.object

   def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['msj'] = 'Estas mascotas se encuentran sin dueño.'
      data['href_eliminar'] = 'apps:private_delete_publicacion'
      return data


@method_decorator([never_cache, login_required()], name='dispatch')
@method_decorator(csrf_exempt, name='post')
@method_decorator(contex_data(title='Nueva Publicación', header='Nueva Publicación'), name='get_context_data')
class PrivateCreateEncontrado(CreateView):
   model = Encontro
   form_class = EncontradoForms
   form_mascota = MascotaForm
   form_ubicacion = UbicacionForm
   template_name = 'private_create_encontrado.html'
   success_url = reverse_lazy('encontrados:private_encontrados')

   def post(self, request, *args, **kwargs):
      form_encontrado = self.form_class(request.POST)
      form_mascota = self.form_mascota(request.POST, files=request.FILES)
      form_ubicacion = self.form_ubicacion(request.POST)
      if form_encontrado.is_valid() and form_mascota.is_valid() and form_ubicacion.is_valid():
         try:
            mascota = form_mascota.save()
            ubicacion = form_ubicacion.save()
            encontrado = form_encontrado.save(commit=False)
            encontrado.id_usuario = self.request.user
            encontrado.id_mascota = mascota
            encontrado.id_ubicacion = ubicacion
            encontrado.save()
            return redirect(to=self.success_url)
         except Exception as err:
            print('¡Ocurrió un error!', str(err))
      else:
         data = {
             'form_class': self.form_class(request.POST),
             'form_mascota': self.form_mascota(request.POST),
             'form_ubicacion': self.form_ubicacion(request.POST),
         }
      return render(request, self.template_name, data)

   def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['msj'] = 'Publica una mascota encontrada.'
      data['form_class'] = self.form_class()
      data['form_mascota'] = self.form_mascota()
      data['form_ubicacion'] = self.form_ubicacion()
      return data


@method_decorator([never_cache, login_required()], name='dispatch')
@method_decorator(csrf_exempt, name='post')
@method_decorator(contex_data(title='Editar Publiación', header='Editar Publicación'),
                  name='get_context_data')
class PrivateUpdateEncontrado(UpdateView):
   model = Encontro
   template_name = 'private_update_encontrado.html'
   success_url = reverse_lazy('encontrados:private_encontrados')
   pk_url_kwarg = 'id'
   form_class = EncontradoForms
   form_mascota = MascotaForm
   form_ubicacion = UbicacionForm

   def dispatch(self, request, *args, **kwargs):
      self.object = get_object_or_404(self.model, id=self.kwargs['id'])
      self.mascota = get_object_or_404(Mascota, id=self.object.id_mascota.id)
      self.ubicacion = get_object_or_404(Ubicacion, id=self.object.id_ubicacion.id)
      return super().dispatch(request, *args, **kwargs)

   def post(self, request, *args, **kwargs):
      form_encontrado = self.form_class(request.POST, instance=self.object)
      form_mascota = self.form_mascota(request.POST, files=request.FILES, instance=self.mascota)
      form_ubicacion = self.form_ubicacion(request.POST, instance=self.ubicacion)
      if form_encontrado.is_valid() and form_mascota.is_valid() and form_ubicacion.is_valid():
         try:
            self.mascota = form_mascota.save()
            self.ubicacion = form_ubicacion.save()
            self.object = form_encontrado.save(commit=False)
            self.object.id_usuario = self.request.user
            self.object.id_mascota = self.mascota
            self.object.id_ubicacion = self.ubicacion
            self.object.save()
            return redirect(to=self.success_url)
         except Exception as err:
            print('¡Ocurrió un error!', str(err))
      else:
         data = self.get_context_data()
         data['msj'] = self.object.id_mascota.especie
         data['form_class'] = self.form_class(request.POST)
         data['form_mascota'] = self.form_mascota(request.POST, files=request.FILES)
         data['form_ubicacion'] = self.form_ubicacion(request.POST)
         return render(request, self.template_name, data)
      return super().post(request, *args, **kwargs)

   def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['msj'] = self.object.id_mascota.especie
      data['form_class'] = self.form_class(instance=self.object)
      data['form_mascota'] = self.form_mascota(instance=self.mascota)
      data['form_ubicacion'] = self.form_ubicacion(instance=self.ubicacion)
      return data


@method_decorator(contex_data(title='Detalle de la publicación'), name='get_context_data')
class PublicDetailEncontrado(DetailView):
   model = Encontro
   template_name = 'public_detail_encontrado.html'
   context_object_name = 'publicacion'
   pk_url_kwarg = 'id'
   query_pk_and_slug = 'id'

   def get_context_data(self, **kwargs):
      data = super().get_context_data(**kwargs)
      data['msj'] = self.object.id_mascota.especie
      data['header'] = self.object.id_mascota.nombre
      data['href_eliminar'] = 'apps:private_delete_publicacion'
      return data