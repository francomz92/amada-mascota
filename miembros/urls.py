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
        auth_views.PasswordChangeView.as_view(template_name='mi_perfil/password_change_form.html'), 
        name='password_change0'),

    path('password_change/done/',
            auth_views.PasswordChangeDoneView.as_view(template_name='mi_perfil/password_change_done.html'), 
            name='password_change_done0'),
    
    path('password/reset/', 
            auth_views.PasswordResetView.as_view(template_name='mi_perfil/password_reset_form.html'), 
            name='password_reset0'),

    path('password_reset/done/', 
            auth_views.PasswordResetDoneView.as_view(template_name='mi_perfil/password_reset_done.html'), 
            name='password_reset_done0'),

    path('password/reset/<uidb64>/<token>/', 
            auth_views.PasswordResetConfirmView.as_view(template_name='mi_perfil/password_reset_confirm.html'), 
            name='password_reset_confirm0'),

    path('password/reset/complete/', 
            auth_views.PasswordResetCompleteView.as_view(template_name='mi_perfil/password_reset_complete.html'), 
            name='password_reset_complete0'),
]

