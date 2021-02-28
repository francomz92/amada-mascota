from django.urls import path
from . import views
#app_name = 'adopcion'
urlpatterns = [
    path('',views.index),
    path('listar/',views.AdopcionList.as_view(),name="adopciones_listar"),
    path('crear/',views.AdopcionCrear.as_view(),name="adopcion_crear"),
]
