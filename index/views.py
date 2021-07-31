from posixpath import join
from django.views.generic.base import TemplateView
from apps.adopcion.models import Adopcion
from apps.encontrados.models import Encontro
from apps.perdidos.models import Perdido
import os
from amada_mascota.settings.Base import BASE_DIR
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'

    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # data['perdidos'] = {'model': 'Perdidos', 'count': Perdido.objects.all().count()}
        # data['encontrados'] = {'model': 'Enocntrados', 'count': Encontro.objects.all().count()}
        # data['adopcion'] = {'model': 'En Adopción', 'count': Adopcion.objects.all().count()}
        data['data'] = [
            {
                'model': 'Perdidos',
                'count': Perdido.objects.all().count(),
                'img': 'static/index/img/lost.jpeg'
            },
            {
                'model': 'Enocntrados',
                'count': Encontro.objects.all().count(),
                'img': 'static/index/img/found.jpg'
            },
            {
                'model': 'En Adopción',
                'count': Adopcion.objects.all().count(),
                'img': 'static/index/img/adopt.jpg'
            },
        ]
        return data
