from django.urls import path
from .views import publicar, lista_encontrados, editar_publicacion, buscar

app_name = 'encontrados'

urlpatterns = [
   path('publicar/', publicar, name='publicar'),
   path('lista_encontrados', lista_encontrados, name='lista_encontrados'),
   path('editar/<id>', editar_publicacion, name='editar_publicacion'),
   path('resultado-busqueda/', buscar, name='buscar'),
]
