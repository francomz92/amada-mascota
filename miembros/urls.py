from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.RegistroUsuario.as_view(), name='register'),
    path('accounts/login/', views.LoginUsuario.as_view(), name='login'),
    path('perfil/',views.perfil,name="perfil"),
    path('editar/',views.perfilActualizar,name='editar'),
    
    path('password/change/', 
        auth_views.PasswordChangeView.as_view(), 
        name='password_change'),

    path('password/change/done/',
            auth_views.PasswordChangeDoneView.as_view(), 
            name='password_change_done'),
    
    path('password/reset/', 
            auth_views.PasswordResetView.as_view(), 
            name='password_reset'),

    path('password/reset/done/', 
            auth_views.PasswordResetDoneView.as_view(), 
            name='password_reset_done'),

    path('password/reset/<uidb64>/<token>/', 
            auth_views.PasswordResetConfirmView.as_view(), 
            name='password_reset_confirm'),

    path('password/reset/complete/', 
            auth_views.PasswordResetCompleteView.as_view(), 
            name='password_reset_complete'),
]

