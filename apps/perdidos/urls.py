from django.urls import path
from . import views

"""urlpatterns = [
    path('agregar/', views.AgregarPublicacion.as_view(), name='agregar')
]
"""

urlpatterns = [
   path('publicar/', views.publicar, name='publicar'),
   path('', views.lista_encontrados, name='lista_encontrados'),
   path('editar/<id>', views.editar_publicacion, name='editar_publicacion'),
   # path('encontrados/resultado-busqueda/', buscar, name='buscar'),
]