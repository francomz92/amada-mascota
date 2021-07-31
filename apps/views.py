from utils.decorators import contex_data
from django.utils.timezone import now
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView, UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from apps.models import Publicacion

# Create your views here.


@method_decorator([never_cache, login_required()], name='dispatch')
class PrivateRenovatePublicacion(UpdateView):
   model = Publicacion

   def dispatch(self, request, *args, **kwargs):
      self.renovar_publicaciones()
      return super().dispatch(request, *args, **kwargs)

   def renovar_publicaciones(self):
      success_url = self.request.META.get('HTTP_REFERER')
      obj = get_object_or_404(self.model, id=self.kwargs['id'], id_usuario=self.request.user)
      if obj.valido_hasta < now().date():
         obj.renovar_fecha_vencimiento()
      return redirect(success_url)


@method_decorator([never_cache, login_required()], name='dispatch')
@method_decorator(csrf_exempt, name='post')
@method_decorator(contex_data(title='Eliminar'), name='get_context_data')
class PrivateDeletePublicacion(DeleteView):
   model = Publicacion
   # template_name = 'private_borrar_perdido.html'
   pk_url_kwarg = 'id'

   def dispatch(self, request, *args, **kwargs):
      self.set_success_url(request)
      return self.delete(request, *args, **kwargs)

   def set_success_url(self, request):
      urls = {
          'adopcion': reverse_lazy('adopcion:private_adopcion'),
          'encontrados': reverse_lazy('encontrados:private_encontrados'),
          'perdidos': reverse_lazy('perdidos:private_perdidos'),
      }
      http_refer = request.META.get('HTTP_REFERER')
      path_refer = http_refer.split('/')[3]
      self.success_url = urls[path_refer]
