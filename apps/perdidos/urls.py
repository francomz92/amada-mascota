from django.urls import path
from .views import publicar, lista_perdidos, editar_publicacion, publicacion, eliminar_publicacion, renovar_publicacion
from .views import buscar_p

app_name = 'perdidos'

urlpatterns = [
   path('publicar/', publicar, name='publicar'),
   path('listar/', lista_perdidos, name='lista_perdidos'),
   path('editar/<id_publicacion>/', editar_publicacion, name='editar_publicacion'),
   path('borrar/<id_publicacion>/', eliminar_publicacion, name='eliminar_publicacion'),
   path('buscar_p/', buscar_p, name='buscar_p'),
   path('publicacion/<id_publicacion>/', publicacion, name='publicacion'),  
   path('renovar/<id_publicacion>/', renovar_publicacion, name='renovar_publicacion'),
]


