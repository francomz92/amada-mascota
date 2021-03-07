from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistroUsuario.as_view(), name='register'),
    path('accounts/login/', views.LoginUsuario.as_view(), name='login'),
    path('perfil/',views.perfil,name="perfil"),
    path('editar/',views.perfilActualizar,name='editar'),
]

