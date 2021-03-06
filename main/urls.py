from django.urls import path, include
from . import views

#magui
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('acerca-de/', views.about, name='about'),
    
    path('suscripciones/', login_required(views.suscripciones), name='suscripciones'),
    path('suscripciones_ver/', login_required(views.suscripciones_ver), name='suscripciones_ver'),
    path('suscripciones_mod/<int:pk>/',login_required(views.SuscripcionModificar.as_view()),name="suscripciones_mod"),

    #path('encontrados/', include('encontrados.urls'))
]
