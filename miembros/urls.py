from django.urls import path
from . import views
from django.contrib.auth.views import login, password_reset, password_reset_done,password_reset_confirm, password_reset_complete

urlpatterns = [
    path('register/', views.RegistroUsuario.as_view(), name='register'),
    path('accounts/login/', views.LoginUsuario.as_view(), name='login'),
    path('perfil/',views.perfil,name="perfil"),
    path('editar/',views.perfilActualizar,name='editar'),
    path('reset/password_reset',password_reset,
        {'template_name':'registration/password_reset_form.html',
        'email_template_name':'registrarion/password_reset_email.html'},
        name='password_reset'),
    path('reset/password_reset_done',password_reset_done,
        {'template_name':'registration/password_reset_done.html'},
        name='password_reset_done'),
    path('reset/<uidb64>[0-9A-Za-z_\-]+/<token>.+',password_reset_confirm,
        {'template_name':'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    path('reset/done',password_reset_complete,
        {'template_name':'registration/password_reset_complete.html'},
        name='password_reset_complete_done')
]

