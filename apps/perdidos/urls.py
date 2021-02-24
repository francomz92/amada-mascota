from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.AgregarPublicacion.as_view(), name='agregar')
]
