from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'adopcion'
urlpatterns = [
    path('',views.index,name="inicio"),
    path('listar/',login_required(views.misAdopciones.as_view()),name="adopciones_listar"),
    path('crear/',login_required(views.AdopcionCrear.as_view()),name="adopcion_crear"),
    path('editar/<int:pk>/',login_required(views.AdopcionActualizar.as_view()),name="adopcion_editar"),
    path('eliminar/<int:pk>/',login_required(views.AdopcionEliminar.as_view()),name="adopcion_eliminar"),
    path('renovar/<int:id>',views.renovar_publicacion,name="adopcion_renovar"),
    path('buscar_a/', views.buscar_a, name='buscar_a'),
]