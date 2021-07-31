from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from utils.decorators import contex_data
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from .models import Suscripcion
from .forms import PrivateSuscripcionesForm

# Create your views here.


@method_decorator(login_required(), name='dispatch')
@method_decorator(contex_data(title='Suscripciones', header='Tus Suscripciones'), name='get_context_data')
class PrivateSuscripciones(ListView):
   model = Suscripcion
   form_class = PrivateSuscripcionesForm
   template_name = 'private_suscripciones.html'
   context_object_name = 'publicaciones'

   def dispatch(self, request, *args, **kwargs):
      if request.method == 'GET':
         return self.get(request, *args, **kwargs)
      elif request.method == 'POST':
         return self.post(request, *args, **kwargs)
      return super().dispatch(request, *args, **kwargs)

   def get_queryset(self):
      self.queryset = self.model.objects.filter(id_usuario=self.request.user)
      return self.queryset

   def get_context_data(self):
      data = {
          'publicaciones': self.queryset,
          'form': self.form_class(),
          'msj': 'Recive notificaciones de tu interes',
          'href_eliminar': 'suscripcion:private_delete_suscripcion'
      }
      return data

   def post(self, request):
      form = self.form_class(request.POST)
      if form.is_valid() and not self.model.objects.filter(id_usuario=self.request.user,
                                                           suscripcion=form.data.get('suscripcion')):
         registro = form.save(commit=False)
         registro.id_usuario = self.request.user
         registro.save()
         return redirect(to='suscripcion:private_suscripcion')
      else:
         form.add_error('suscripcion', '¡Ya tienes esta suscripción activa!')
         data = self.get_context_data()
         data['form'] = form
         data['publicaciones'] = self.get_queryset()
         return render(request, 'private_suscripciones.html', data)


class PrivateDeleteSuscripcion(DeleteView):
   model = Suscripcion
   pk_url_kwarg = 'id'
   success_url = reverse_lazy('suscripcion:private_suscripcion')

   def dispatch(self, request, *args, **kwargs):
      return self.delete(request, *args, **kwargs)