from django.urls import path
from . import views

from django.conf.urls import url  #magui

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.about, name='about'),
    path('consultas/',views.consultas, name='consultas'),
    url(r'^consultas_perdidos/$',views.ConsultasPerdidosView.as_view(), name='consultas_perdidos'),
    url(r'^consultas_encontrados/$',views.ConsultasEncontradosView.as_view(), name='consultas_encontrados'),
]
