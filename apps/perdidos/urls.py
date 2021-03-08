from django.urls import path
from . import views

"""urlpatterns = [
    path('agregar/', views.AgregarPublicacion.as_view(), name='agregar')
]
"""
app_name = 'perdidos'

urlpatterns = [
   path('publicar/', views.publicar, name='publicar'),
   path('', views.lista_encontrados, name='lista_perdidos'),
   path('editar/<id>', views.editar_publicacion, name='editar_publicacion'),
   path('buscar/', views.buscar_p, name='buscar_perdidos')
   # path('encontrados/resultado-busqueda/', buscar, name='buscar'),
]