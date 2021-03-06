from django.urls import path
from .views import publicar, lista_encontrados, editar_publicacion, publicacion, eliminar_publicacion, renovar_publicacion

app_name = 'encontrados'

urlpatterns = [
   path('publicar/', publicar, name='publicar'),
   path('', lista_encontrados, name='lista_encontrados'),
   path('editar/<id_publicacion>/', editar_publicacion, name='editar_publicacion'),
   path('<id_publicacion>/', publicacion, name='publicacion'),
   path('borrar/<id_publicacion>/', eliminar_publicacion, name='eliminar_publicacion'),
   path('renovar/<id_publicacion>/', renovar_publicacion, name='renovar_publicacion'),
]
