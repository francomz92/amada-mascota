from django.urls import path
from .views import publicar, lista_encontrados, editar_publicacion

app_name = 'encontrados'

urlpatterns = [
   path('encontrados/publicar', publicar, name='publicar'),
   path('encontrados/', lista_encontrados, name='lista_encontrados'),
   path('encontrados/editar/<id=id_publicacion>', editar_publicacion, name='editar_publicacion'),
]
