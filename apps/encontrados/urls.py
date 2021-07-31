from django.urls import path
from .views import PrivateCreateEncontrado, PrivateEncontrados, PrivateUpdateEncontrado, PublicDetailEncontrado, PublicEncontrados

app_name = 'encontrados'

urlpatterns = [
    path(
        'encontrados/',
        PublicEncontrados.as_view(),
        name='public_encontrados',
    ),
    path(
        'encontrados/mis-publicaciones/',
        PrivateEncontrados.as_view(),
        name='private_encontrados',
    ),
    path(
        'encontrados/publicar/',
        PrivateCreateEncontrado.as_view(),
        name='private_create_encontrados',
    ),
    path(
        'encontrados/editar/<int:id>/',
        PrivateUpdateEncontrado.as_view(),
        name='private_update_encontrados',
    ),
    path(
        'encontrados/<int:id>/',
        PublicDetailEncontrado.as_view(),
        name='public_detail_encontrados',
    ),
]