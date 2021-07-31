from django.urls import path
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

reset_urls = [
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='reset_password/reset_password.html'),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='reset_password/reset_password_done.html'),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='reset_password/reset_password_confirm.html'),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='reset_password/reset_password_comlete.html'),
        name='password_reset_complete',
    ),
]