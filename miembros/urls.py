from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistroUsuario.as_view(), name='register'),
    path('login/', views.LoginUsuario.as_view(), name='login'),
]
