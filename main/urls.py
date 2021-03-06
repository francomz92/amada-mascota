from django.urls import path, include
from . import views

from django.conf.urls import url  #magui

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.about, name='about'),
    
    path('consultas_perdidos/', views.consultas_perdidos, name='consultas_perdidos'),
    url(r'^consultas_encontrados/$',views.ConsultasEncontradosView.as_view(), name='consultas_encontrados'),
    
    path('suscripciones/', views.suscripciones, name='suscripciones'),
    path('suscripciones_ver/', views.suscripciones_ver, name='suscripciones_ver'),


    #path('encontrados/', include('encontrados.urls'))
]
