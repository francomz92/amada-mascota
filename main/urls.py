from django.urls import path
from . import views

from django.conf.urls import url  #magui

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.about, name='about'),
    path('busquedas/',views.busquedas, name='busquedas'),
    url(r'^busquedas_perdidos/$',views.BusquedasPerdidosView.as_view(), name='busquedas_perdidos'),
]
