from django.urls import path
from apps.usuario.views import UserProfile, UserUpdate

profile_urls = [
    path(
        'perfil/<slug:username>/',
        UserProfile.as_view(),
        name='private_user_profile',
    ),
    path(
        'perfil/<slug:username>/editar/',
        UserUpdate.as_view(),
        name='private_user_update',
    ),
]