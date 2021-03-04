from django.urls import path, include
from . import views

from django.conf.urls import url  #magui

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.about, name='about'),
    url(r'^consultas_perdidos/$',views.consultas_perdidos, name='consultas_perdidos'),
    url(r'^consultas_encontrados/$',views.ConsultasEncontradosView.as_view(), name='consultas_encontrados'),
]
