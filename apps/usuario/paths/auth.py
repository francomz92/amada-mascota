from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
from apps.usuario.views import SignUp

auth_urls = [
    path(
        'login/',
        LoginView.as_view(template_name='authentication/login.html', redirect_authenticated_user=True),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='authentication/logout.html'),
        name='logout',
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='change_password/change_password_done.html'),
        name='password_change',
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='change_password/change_password.html'),
        name='password_cange_complete',
    ),
    path(
        'sign-up/',
        SignUp.as_view(),
        name='sign_up',
    ),
]